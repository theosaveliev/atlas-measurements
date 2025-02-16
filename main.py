import datetime
import os
import time
from dataclasses import dataclass
from typing import Callable

import requests

gcp_targets = {
    '104.199.6.64': 'Belgium (europe-west1)',
    '35.197.249.117': 'London (europe-west2)',
    '34.107.50.245': 'Frankfurt (europe-west3)',
    '34.91.152.13': 'Netherlands (europe-west4)',
    '34.65.99.193': 'Zurich (europe-west6)',
    '34.154.116.236': 'Milan (europe-west8)',
    '34.155.160.66': 'Paris (europe-west9)',
    '34.118.88.136': 'Warsaw (europe-central2)',
    '35.228.50.108': 'Finland (europe-north1)',
    '35.247.10.221': 'Oregon (us-west1)',
    '35.235.83.92': 'Los Angeles (us-west2)',
    '34.106.60.77': 'Salt Lake City (us-west3)',
    '34.125.243.211': 'Las Vegas (us-west4)',
    '34.72.28.29': 'Iowa (us-central1)',
    '34.75.166.194': 'South Carolina (us-east1)',
    '35.245.110.238': 'Northern Virginia (us-east4)',
    '34.95.32.67': 'Montreal (northamerica-northeast1)',
    '34.124.121.68': 'Toronto (northamerica-northeast2)',
    '35.199.77.203': 'Sao Paulo (southamerica-east1)',
    '34.176.193.97': 'Santiago (southamerica-west1)',
    '34.93.102.253': 'Mumbai (asia-south1)',
    '34.131.40.9': 'Delhi (asia-south2)',
    '34.87.108.57': 'Singapore (asia-southeast1)',
    '34.101.77.131': 'Jakarta (asia-southeast2)',
    '35.229.225.152': 'Taiwan (asia-east1)',
    '35.220.133.61': 'Hong Kong (asia-east2)',
    '35.189.147.253': 'Tokyo (asia-northeast1)',
    '34.97.77.117': 'Osaka (asia-northeast2)',
    '34.64.75.27': 'Seoul (asia-northeast3)',
    '35.201.23.39': 'Sydney (australia-southeast1)',
    '34.129.68.226': 'Melbourne (australia-southeast2)'
}


@dataclass
class Definition:
    target: str
    description: str
    type: str
    af: int
    is_oneoff: bool
    start_time: int


@dataclass
class Probe:
    requested: int
    type: str
    value: str


def create_payload(definitions: list, probes: list) -> dict:
    return {
        "definitions": [vars(d) for d in definitions],
        "probes": [vars(p) for p in probes]
    }


def create_measurements(api_url: str, headers: dict, payload: dict) -> list:
    resp = requests.post(url=api_url, headers=headers, json=payload).json()
    return resp['measurements']


def gather_measurements(api_url: str, mids: list, callb: Callable) -> list:
    result = []
    for mid in mids:
        resp = requests.get(f'{api_url}/{mid}/latest/').json()
        if len(resp) > 0:
            result.append(callb(resp))
    return result


def reduce_avg_rtt(measurement: list) -> float:
    rtt = []
    for probe in measurement:
        last_hop = max(probe['result'], key=lambda res: res['hop'])
        rtt.extend(map(lambda res: res.get('rtt', None), last_hop['result']))
    rtt = list(filter(None, rtt))
    return -1.0 if len(rtt) == 0 else sum(rtt) / len(rtt)


def reduce_region(measurement: list, targets: dict) -> str:
    return targets[measurement[0]['dst_addr']]


def reduce_url(measurement: list, msm_url: str) -> str:
    return f'{msm_url}/{measurement[0]["msm_id"]}'


def _create_trace(targets: dict, start_time: int) -> list:
    result = []
    for ip, desc in targets.items():
        result.append(Definition(
            target=ip,
            description=desc,
            type='traceroute',
            af=4,
            is_oneoff=True,
            start_time=start_time
        ))
    return result


def main():
    base_url = os.getenv("BASE_URL")
    api_url = f'{base_url}/api/v2/measurements'
    headers = {'Authorization': f'Key {os.getenv("API_KEY")}'}
    schedule = datetime.datetime.now() + datetime.timedelta(minutes=1)
    timestamp = int(time.mktime(schedule.timetuple()))
    trace = _create_trace(gcp_targets, timestamp)
    probes = [
        Probe(20, 'country', 'GE'),
        # Probe(2, 'country', 'SE'),
        # Probe(3, 'probes', '11111,22222,33333'),
    ]
    payload = create_payload(trace, probes)
    mids = create_measurements(api_url, headers, payload)

    print(f'mids={mids}')
    time.sleep(900)

    def transform(measurement: list):
        return (
            reduce_avg_rtt(measurement),
            reduce_region(measurement, gcp_targets),
            reduce_url(measurement, f'{base_url}/measurements')
        )

    measurements = gather_measurements(api_url, mids, transform)
    for res in sorted(measurements, key=lambda r: r[0]):
        print(f'{res[0]:.1f},{res[1]},{res[2]}')


if __name__ == '__main__':
    main()
