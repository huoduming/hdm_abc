#!usr/bin/dev python
# -*- coding: UTF-8 -*-

import csv

def csv_write(data,filename):
    with open(filename,"wb") as csv_file:
        writer = csv.writer(csv_file,delimiter=',')
        for line in data:
            writer.writerow(line)

if __name__=="__main__":
    data = []
    with open('data.txt') as f:
        for line in f :
            data.append(line.strip().split(","))
    print data
    filename = 'output.csv'
    csv_write(data,filename)
