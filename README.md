# Network Rail Freight Schedule 

## Aim of project 

To find out what freight trains pass any uk station on that day.

Sadly as found out during development, the network rail working schedule
is a list of all possible trains that could run, the reality is that alot
less will actually run and their actual times will vary greatly.

## pre reqs 
A free network account is needed, sign up with the following link  
https://publicdatafeeds.networkrail.co.uk/ntrod/welcome

the credentials provide will need to be added to the auth.py file 
replacing the following 
```
feed_username='myusername@mail.com'
feed_password='xxxxxxx-yyyyyyy-xxxxxx'
```

## How To Run 

```commandline
Python3 app.py 
```



## Debugging / Help 

json format example
https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_ALL_FULL_DAILY&day=toc-full
CF formatt example 
https://publicdatafeeds.networkrail.co.uk/ntrod/CifFileAuthenticate?type=CIF_ALL_FULL_DAILY&day=toc-full.CIF.gz