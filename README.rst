atlas-measurements
******************

Did you ever wonder which GCP region to choose to get the best service in
Tbilisi?

`The map <https://cloud.google.com/about/locations>`_ is uncertain,
so I've run a couple of tests.

Test 1
======

First draft.

Test date: Dec 20th, 2022.

Test subjects:

1. AS35805 JSC "Silknet"
2. AS16010 Magticom Ltd.
3. AS20545 GRENA

Test goal:
Identify lowest RTT region.

Test results:

=========  ========================  ===============================================
RTT (avg)  Region                    Raw data
=========  ========================  ===============================================
64         Frankfurt (europe-west3)  https://atlas.ripe.net/measurements/47965756/
68         Zurich (europe-west6)     https://atlas.ripe.net/measurements/47966050/
69         Milan (europe-west8)      https://atlas.ripe.net/measurements/47966049/
74         Belgium (europe-west1)    https://atlas.ripe.net/measurements/47966052/
76         Paris (europe-west9)      https://atlas.ripe.net/measurements/47966053/
76         Warsaw (europe-central2)  https://atlas.ripe.net/measurements/47966046/
172        Iowa (us-central1)        https://atlas.ripe.net/measurements/47966054/
315        Mumbai (asia-south1)      https://atlas.ripe.net/measurements/47966047/
326        Delhi (asia-south2)       https://atlas.ripe.net/measurements/47966051/
=========  ========================  ===============================================


Test 2
======

Test time was synchronized, test subjects were narrowed to Magti and Silknet,
more regions were included.

Test date: Jan 18th, 2023.

Test subjects:

1. AS35805 JSC "Silknet"
2. AS16010 Magticom Ltd.

Test goal:
Identify lowest RTT GCP region.

Test results:

=========  ===========================  ===============================================
RTT (avg)  Region                       Raw data
=========  ===========================  ===============================================
69.7       Frankfurt (europe-west3)     https://atlas.ripe.net/measurements/48863139
70.9       Zurich (europe-west6)        https://atlas.ripe.net/measurements/48863140
71.0       Milan (europe-west8)         https://atlas.ripe.net/measurements/48863141
78.2       Netherlands (europe-west4)   https://atlas.ripe.net/measurements/48863145
80.6       Warsaw (europe-central2)     https://atlas.ripe.net/measurements/48863144
80.6       Belgium (europe-west1)       https://atlas.ripe.net/measurements/48863142
81.4       London (europe-west2)        https://atlas.ripe.net/measurements/48863147
81.9       Paris (europe-west9)         https://atlas.ripe.net/measurements/48863143
98.8       Finland (europe-north1)      https://atlas.ripe.net/measurements/48863146
176.9      Iowa (us-central1)           https://atlas.ripe.net/measurements/48863148
313.2      Mumbai (asia-south1)         https://atlas.ripe.net/measurements/48863150
313.8      Singapore (asia-southeast1)  https://atlas.ripe.net/measurements/48863152
326.8      Delhi (asia-south2)          https://atlas.ripe.net/measurements/48863151
=========  ===========================  ===============================================


Test 3
======

All GE probes were requested.

Test date: Jan 18th, 2023.

Test subjects:

1. AS16010 Magticom Ltd.
2. AS203136 LLC Ordunet
3. AS20545 GRENA
4. AS44491 ZAO "Aquafon-GSM"
5. AS208320 AIRMAX LLC
6. AS35805 JSC "Silknet"

Test goal:
Identify lowest RTT GCP region.

Test results:

=========  ===========================  ===============================================
RTT (avg)  Region                       Raw data
=========  ===========================  ===============================================
70.9       Frankfurt (europe-west3)     https://atlas.ripe.net/measurements/48874702
74.2       Zurich (europe-west6)        https://atlas.ripe.net/measurements/48874703
75.3       Milan (europe-west8)         https://atlas.ripe.net/measurements/48874704
75.7       Netherlands (europe-west4)   https://atlas.ripe.net/measurements/48874708
78.7       Belgium (europe-west1)       https://atlas.ripe.net/measurements/48874705
80.3       Paris (europe-west9)         https://atlas.ripe.net/measurements/48874706
81.6       Warsaw (europe-central2)     https://atlas.ripe.net/measurements/48874707
81.9       London (europe-west2)        https://atlas.ripe.net/measurements/48874710
93.9       Finland (europe-north1)      https://atlas.ripe.net/measurements/48874709
179.5      Iowa (us-central1)           https://atlas.ripe.net/measurements/48874711
323.7      Singapore (asia-southeast1)  https://atlas.ripe.net/measurements/48874714
328.6      Mumbai (asia-south1)         https://atlas.ripe.net/measurements/48874712
346.9      Delhi (asia-south2)          https://atlas.ripe.net/measurements/48874713
=========  ===========================  ===============================================


Test 4
======

All GE probes worldwide.

Test date: Jan 18th, 2023.

Test subjects:

1. AS16010 Magticom Ltd.
2. AS203136 LLC Ordunet
3. AS20545 GRENA
4. AS44491 ZAO "Aquafon-GSM"
5. AS208320 AIRMAX LLC
6. AS35805 JSC "Silknet"

Test goal:
Identify lowest RTT GCP region.

Test results:

=========  ==================================  ===============================================
RTT (avg)  Region                              Raw data
=========  ==================================  ===============================================
68.2       Frankfurt (europe-west3)            https://atlas.ripe.net/measurements/48879393
75.6       Netherlands (europe-west4)          https://atlas.ripe.net/measurements/48879394
76.5       Belgium (europe-west1)              https://atlas.ripe.net/measurements/48879391
77.0       Milan (europe-west8)                https://atlas.ripe.net/measurements/48879396
77.0       Zurich (europe-west6)               https://atlas.ripe.net/measurements/48879395
79.3       Warsaw (europe-central2)            https://atlas.ripe.net/measurements/48879398
81.6       Paris (europe-west9)                https://atlas.ripe.net/measurements/48879397
85.5       London (europe-west2)               https://atlas.ripe.net/measurements/48879392
97.1       Finland (europe-north1)             https://atlas.ripe.net/measurements/48879399
156.3      Montreal (northamerica-northeast1)  https://atlas.ripe.net/measurements/48879407
159.7      Northern Virginia (us-east4)        https://atlas.ripe.net/measurements/48879406
165.9      South Carolina (us-east1)           https://atlas.ripe.net/measurements/48879405
168.0      Toronto (northamerica-northeast2)   https://atlas.ripe.net/measurements/48879408
177.7      Iowa (us-central1)                  https://atlas.ripe.net/measurements/48879404
204.3      Salt Lake City (us-west3)           https://atlas.ripe.net/measurements/48879402
214.9      Oregon (us-west1)                   https://atlas.ripe.net/measurements/48879400
216.4      Las Vegas (us-west4)                https://atlas.ripe.net/measurements/48879403
224.4      Los Angeles (us-west2)              https://atlas.ripe.net/measurements/48879401
273.6      Sao Paulo (southamerica-east1)      https://atlas.ripe.net/measurements/48879409
280.3      Santiago (southamerica-west1)       https://atlas.ripe.net/measurements/48879410
309.6      Tokyo (asia-northeast1)             https://atlas.ripe.net/measurements/48879417
314.5      Osaka (asia-northeast2)             https://atlas.ripe.net/measurements/48879418
320.9      Taiwan (asia-east1)                 https://atlas.ripe.net/measurements/48879415
322.4      Hong Kong (asia-east2)              https://atlas.ripe.net/measurements/48879416
328.5      Singapore (asia-southeast1)         https://atlas.ripe.net/measurements/48879413
331.4      Seoul (asia-northeast3)             https://atlas.ripe.net/measurements/48879419
338.3      Jakarta (asia-southeast2)           https://atlas.ripe.net/measurements/48879414
346.4      Mumbai (asia-south1)                https://atlas.ripe.net/measurements/48879411
354.2      Sydney (australia-southeast1)       https://atlas.ripe.net/measurements/48879420
358.8      Melbourne (australia-southeast2)    https://atlas.ripe.net/measurements/48879421
362.0      Delhi (asia-south2)                 https://atlas.ripe.net/measurements/48879412
=========  ==================================  ===============================================


Test 5
======

Magti, Silknet, Tbilisi, - similar to #2.

Test date: Jan 18th, 2023.

Test subjects:

1. AS35805 JSC "Silknet"
2. AS16010 Magticom Ltd.

Test goal:
Identify lowest RTT GCP region.

Test results:

=========  ===========================  ===============================================
RTT (avg)  Region                       Raw data
=========  ===========================  ===============================================
68.7       Frankfurt (europe-west3)     https://atlas.ripe.net/measurements/48880655
73.5       Zurich (europe-west6)        https://atlas.ripe.net/measurements/48880657
74.1       Milan (europe-west8)         https://atlas.ripe.net/measurements/48880658
77.9       Belgium (europe-west1)       https://atlas.ripe.net/measurements/48880653
78.5       Paris (europe-west9)         https://atlas.ripe.net/measurements/48880659
80.1       Warsaw (europe-central2)     https://atlas.ripe.net/measurements/48880660
80.8       London (europe-west2)        https://atlas.ripe.net/measurements/48880654
81.0       Netherlands (europe-west4)   https://atlas.ripe.net/measurements/48880656
100.5      Finland (europe-north1)      https://atlas.ripe.net/measurements/48880661
=========  ===========================  ===============================================


Test 6
======

Magti, Silknet, Tbilisi, - similar to #2.

Test date: Jan 31th, 2023.

Test subjects:

1. AS35805 JSC "Silknet"
2. AS16010 Magticom Ltd.

Test goal:
Identify lowest RTT GCP region.

Test results:

=========  ===========================  ===============================================
RTT (avg)  Region                       Raw data
=========  ===========================  ===============================================
64.2       Frankfurt (europe-west3)     https://atlas.ripe.net/measurements/49294875
65.5       Zurich (europe-west6)        https://atlas.ripe.net/measurements/49294877
71.1       Milan (europe-west8)         https://atlas.ripe.net/measurements/49294878
71.2       Netherlands (europe-west4)   https://atlas.ripe.net/measurements/49294876
74.8       Belgium (europe-west1)       https://atlas.ripe.net/measurements/49294873
76.9       Paris (europe-west9)         https://atlas.ripe.net/measurements/49294879
79.0       London (europe-west2)        https://atlas.ripe.net/measurements/49294874
80.1       Warsaw (europe-central2)     https://atlas.ripe.net/measurements/49294880
95.9       Finland (europe-north1)      https://atlas.ripe.net/measurements/49294881
=========  ===========================  ===============================================
