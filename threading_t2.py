#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import time
import threading

def get_site_code(url):
    r = requests.get(url)
    status = r.status_code
    line = url + '' + str(status)
    with open('/tmp/site_status.txt','a+') as f:
        f.writelines(line + '\n')

if __name__ == '__main__':
    print 'Starting at:',time.ctime()
    threads = []

    for url in open('./url.txt'):
        url = url.strip()
        t = threading.Thread(target=get_site_code,args=(url,))
        threads.append(t)

    for i in range(len(threads)):
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()

    print 'Done at:',time.ctime()

