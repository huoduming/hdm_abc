#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import os.path


def create_shell(src, des):
    if os.path.exists('./do.sh'):
        os.remove('./do.sh')
    with open('./do.sh', 'a') as f:
        print >> f, '#!/bin/bash'
        print >> f, 'rsync -avzP{0} 1.1.1.1:{1}/'.format(src,des)

def read_shell():
    rs = open('./do.sh')
    for line in rs:
        print line
    rs.close()

if __name__ == '__main__':
    create_shell('/data', '/data')
    read_shell()
