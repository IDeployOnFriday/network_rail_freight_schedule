A project which will interrogate the realtimetrains api for freight movements 

example curl request 
https://api.rtt.io/api/v1/json/search/search/detailed/gb-nr:BHM?stp=WVS&show=freight&order=wtt

 https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_FREIGHT_FULL_DAILY&day=toc-full


{'serviceUid': 'H31618', 'runDate': '2023-12-07', 'serviceType': 'train', 'isPassenger': False, 'trainIdentity': '3S26',
'powerType': 'D', 'atocCode': 'ZZ', 'atocName': 'Unknown', 'performanceMonitored': True, 'origin': 
[{'tiploc': 'LEEDS', 'description': 'Leeds', 'workingTime': '062500'}], 
'destination': [{'tiploc': 'YORKCRW', 'description': 'York Thrall Europa', 'workingTime': '072600'}], 
'realtimeActivated': True, 'runningIdentity': '3S26'}
