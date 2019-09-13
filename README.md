#Purpose

This is a simple POC to write several thousand of points per second to InfluxDB over UDP

`curl -X GET "http://127.0.0.1:8086/query?q=select+count("swf_call")+from+moult_points&db=storm" | jq .`

`curl -X GET "http://127.0.0.1:8086/query?q=select+sum("swf_call")+from+moult_points+group+by+time(1s)&db=storm" | jq`
