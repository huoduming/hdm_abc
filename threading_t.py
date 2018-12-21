#!/usr/bin/env python
# -*- coding: UTF8 -*-
import requests
import time


def get_site_code(url):
    r = requests.get(url)
    status = r.status_code
    line = url + ' '+ str(status)
    with open('/tmp/site_status.txt','a+') as f:
        f.writelines(line + '\n')

if __name__ == '__main__':
    print 'string at:',time.ctime()
    for url in open('./url.txt'):
        url = url.strip()
        get_site_code(url)

print 'Done al:',time.ctime()


'''def get_site_code(url):
    r = requests.get(url)
    status = r.status_code

    line = url + ' ' + str(status)

    with open('/tmp/site_stauts.txt', 'a+') as f:
        f.writelines(line + '\n')


if __name__ == '__main__':

    print 'starting at:', time.ctime()

    for url in open('./url.txt'):
        url = url.strip()

        get_site_code(url)

    print 'Done at:', time.ctime()'''