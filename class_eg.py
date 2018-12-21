#!/usr/bin/env python
# -*- coding: UTF8-*-
'''class Car(object):
    def __init__(self,company,brand,year,orgin_miles):
        self.company = company
        self.brand = brand
        self.year = year
        self.orgin_miles = orgin_miles

    def get_car_info(self):
        print self.company + ' ' + self.brand + ' ' + str(self.year) + ' yunxing ' + str(self.orgin_miles)

if __name__ == '__main__':

    my_car = Car('dazhong','audi',2018,20000)
    my_car.get_car_info() '''


class Car(object):
    def __init__(self, company, brand, year):
        self.company = company
        self.brand = brand
        self.year = year

    def get_car_info(self):
        print self.company + ' ' + self.brand + ' ' + str(self.year)

    def petrol_used(self):
        print 'You done not neet to add petrol,lt is enough'


class EvCar(Car):
    def __init__(self, company, brand, year):
        super(EvCar, self).__init__(company, brand, year)  # 可以使用方法A
        Car.__init__(self, company, brand, year)  # 可以使用方法B

    def petrol_used(self):
        print 'I do not used petrol，I only used electric'


if __name__ == '__main__':
    '''my_car = Car('jili','volvo',2018)
    my_car.get_car_info()
    my_car.petrol_used()'''
    byd = EvCar('byd', 'qin', 2019)
    byd.get_car_info()
    byd.petrol_used()
