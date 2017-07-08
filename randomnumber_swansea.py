#this is a script to assign randomly people from cohort 8 to our rooms in Swansea. It took me hours to do this stupid thing
#enjoy your trips to swansea babes

import random

Cohort8 = ['Chris', 'Dave', 'Fra', 'Joel', 'Li', 'Luke', 'Matyas', 'Qiao', 'Sam', 'Sozos']
Room_1 = []
Room_2 = []
Room_3 = []

def firstroom():
    n = 10
    while len(Cohort8) > 8:
        a = Cohort8[random.randrange(0, n)]
        Room_1.append(a)
        Cohort8.remove(a)
        n -= 1
    return Room_1

def secondroom():
    n = 8
    while len(Cohort8) > 5:
        b = Cohort8[random.randrange(0, n)]
        Room_2.append(b)
        Cohort8.remove(b)
        n -= 1
    return Room_2

def thirdroom():
    n = 5
    while len(Cohort8) > 0:
        c = Cohort8[random.randrange(0, n)]
        Room_3.append(c)
        Cohort8.remove(c)
        n -= 1
    return Room_3

print "In the first room there are", firstroom()
print "In the second room there are", secondroom()
print "In the third room there are", thirdroom()
print "Have a nice trip folks!"

