import datetime
import time

import pytest

from main import (Definition, Probe, create_payload, create_measurements,
                  reduce_avg_rtt, reduce_region, reduce_url)


@pytest.fixture
def targets():
    return {'172.16.0.1': 'Region 1'}


@pytest.fixture
def timestamp():
    schedule = datetime.datetime.now() + datetime.timedelta(minutes=1)
    return int(time.mktime(schedule.timetuple()))


@pytest.fixture
def trace_definition(timestamp):
    return Definition(
        target="172.16.0.1",
        description="Region 1",
        type="traceroute",
        af=4,
        is_oneoff=True,
        start_time=timestamp
    )


@pytest.fixture
def probe():
    return Probe(1, 'probes', '11111')


@pytest.fixture
def payload(trace_definition, probe):
    return {
        "definitions": [vars(trace_definition)],
        "probes": [vars(probe)]
    }


def test_create_payload(payload, trace_definition, probe):
    assert payload == create_payload([trace_definition], [probe])


@pytest.fixture
def mid():
    return 11122233


def test_create_measurements(requests_mock, payload, mid):
    api_url = 'mock://atlas.local/api/v2/measurements'
    headers = {'Authorization': 'Key 11111111-2222-3333-4444-555555555555'}
    trace_response = {'measurements': [mid]}
    requests_mock.post(url=api_url, headers=headers, json=trace_response)
    assert [mid] == create_measurements(api_url, headers, payload)


@pytest.fixture
def measurement(timestamp, mid):
    return [
        {
            "fw": 5080,
            "mver": "2.6.2",
            "lts": 0,
            "endtime": timestamp,
            "dst_name": "172.16.0.1",
            "dst_addr": "172.16.0.1",
            "src_addr": "10.0.0.1",
            "proto": "ICMP",
            "af": 4,
            "size": 48,
            "paris_id": 1,
            "result": [
                {
                    "hop": 1,
                    "result": [
                        {
                            "from": "192.168.0.100",
                            "ttl": 254,
                            "size": 76,
                            "rtt": 1.0
                        }
                    ]
                }
            ],
            "msm_id": mid,
            "prb_id": 11111,
            "timestamp": timestamp,
            "msm_name": "Traceroute",
            "from": "10.0.100.1",
            "type": "traceroute",
            "group_id": mid,
            "stored_timestamp": timestamp
        }
    ]


def test_reduce_avg_rtt(measurement):
    assert 1.0 == reduce_avg_rtt(measurement)
    del measurement[0]["result"][0]["result"][0]["rtt"]
    assert -1.0 == reduce_avg_rtt(measurement)


def test_reduce_region(measurement, targets):
    assert 'Region 1' == reduce_region(measurement, targets)


def test_reduce_url(measurement, mid):
    msm_url = 'mock://atlas.local/measurements'
    assert f'{msm_url}/{mid}' == reduce_url(measurement, msm_url)
