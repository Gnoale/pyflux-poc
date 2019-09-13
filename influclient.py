#!/usr/bin/env python

# -*- coding: utf-8 -*-
from influxdb import InfluxDBClient

from multiprocessing import Pool

# testing purpose
import socket, random, os

def main(host='localhost'):
 
    client = InfluxDBClient(host, use_udp=True, udp_port=8089)

    #line_body = ["moult_points,host={},region=laborde simple_point={}".format(socket.gethostname(), random.randint(0,2000))]


    line_body = ["moult_points,host={},region=laborde swf_call=1".format(socket.gethostname())]

    print(line_body)


    pool = Pool(processes=1)

    for i in range(1000):
        pool.apply_async(client.send_packet(line_body, protocol=u'line'))

if __name__ == '__main__':
    main()
