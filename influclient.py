#!/usr/bin/env python

# -*- coding: utf-8 -*-
from influxdb import InfluxDBClient
from multiprocessing import Pool
import socket, random, os
import functools
import time
from threading import Thread


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.clock()    # 1
        value = func(*args, **kwargs)
        end_time = time.clock()      # 2
        run_time = end_time - start_time    # 3
        print("Finished {0!r} in {1:.4f} secs".format(func.__name__, run_time ))
        return value
    return wrapper_timer


client = InfluxDBClient('localhost', use_udp=True, udp_port=8089)
#line_body = ["moult_points,host={},region=laborde simple_point={}".format(socket.gethostname(), random.randint(0,2000))]
line_body = ["moult_points,host={},region=laborde swf_call=1".format(socket.gethostname())]


@timer
def push_data(client=client, data=line_body):
    #pool = Pool(1)
    for i in range(1000):
        #pool.apply_async(client.send_packet(data, protocol=u'line'))
        Thread(target=client.send_packet(data, protocol=u'line'))

    #pool.close() 


if __name__ == '__main__':
    while True:
        push_data()
