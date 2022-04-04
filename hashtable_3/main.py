import datetime , random , string
from msilib.schema import Error
from random import randint
from time import time, time_ns
from Hashtable import *

if __name__ == "__main__":

    english_small = []
    english_large = []
    small_read_time = []
    large_read_time = []
    small_hash_time = []
    large_hash_time = []

    small_txt_counter = 0
    large_txt_counter = 0
    table_size = None

    start = datetime.datetime.now();
    with open('English_small.txt') as small_file:
        for line in small_file:
            line = line.rstrip()
            if(len(line) > 0):
                english_small.append(line)
        small_file.close()
    end = datetime.datetime.now()
    time_dif = end - start
    small_read_time = time_dif.total_seconds() * 1000


    start = datetime.datetime.now();
    with open('English_large.txt') as large_file:
        for line in large_file:
            line = line.rstrip()
            if(len(line) > 0):
                english_large.append(line)
        large_file.close()
    end = datetime.datetime.now()
    time_dif = end - start
    large_read_time = time_dif.total_seconds() * 1000

    
    table_size = 200000
    i = 1
    hash_time = None
    start = datetime.datetime.now()
    hash_time = Hashtable(table_size)
    for line in english_small:
        try:
            hash_time.__setitem__(i,line)
        except  Exception as e:
            print(e)
        i += 1
    end = datetime.datetime.now()
    time_dif = end - start
    small_hash_time.append(format((small_read_time + time_dif.total_seconds() * 1000), '.2f') + ' ms')


    table_size = 300000
    i = 1
    hash_time = None
    start = datetime.datetime.now()
    hash_time = Hashtable(table_size)
    for line in english_small:
        try:
            hash_time.__setitem__(i,line)
        except  Exception as e:
            print(e)
        i += 1
    end = datetime.datetime.now()
    time_dif = end - start
    small_hash_time.append(format((small_read_time + time_dif.total_seconds() * 1000), '.2f') + ' ms')


    table_size = 400000
    i = 1
    hash_time = None
    start = datetime.datetime.now()
    hash_time = Hashtable(table_size)
    for line in english_small:
        try:
            hash_time.__setitem__(i,line)
        except  Exception as e:
            print(e)
        i += 1
    end = datetime.datetime.now()
    time_dif = end - start
    small_hash_time.append(format((small_read_time + time_dif.total_seconds() * 1000), '.2f') + ' ms')


    table_size = 200000
    i = 1
    hash_time = None
    start = datetime.datetime.now()
    hash_time = Hashtable(table_size)
    for line in english_large:
        try:
            hash_time.__setitem__(i,line)
        except  Exception as e:
            print(e)
        i += 1
    end = datetime.datetime.now()
    time_dif = end - start
    large_hash_time.append(format((large_read_time + time_dif.total_seconds() * 1000), '.2f') + ' ms')


    table_size = 300000
    i = 1
    hash_time = None
    start = datetime.datetime.now()
    hash_time = Hashtable(table_size)
    for line in english_large:
        try:
            hash_time.__setitem__(i,line)
        except  Exception as e:
            print(e)
        i += 1
    end = datetime.datetime.now()
    time_dif = end - start
    large_hash_time.append(format((large_read_time + time_dif.total_seconds() * 1000), '.2f') + ' ms')


    table_size = 400000
    i = 1
    hash_time = None
    start = datetime.datetime.now()
    hash_time = Hashtable(table_size)
    for line in english_large:
        try:
            hash_time.__setitem__(i,line)
        except  Exception as e:
            print(e)
        i += 1
    end = datetime.datetime.now()
    time_dif = end - start
    large_hash_time.append(format((large_read_time + time_dif.total_seconds() * 1000), '.2f') + ' ms')

    table_size = 100000
    set = set()
    while len(set) < 100000:
        set.add(randint(1,100000))
    set = list(set)

    linear = Hashtable(table_size)
    double = Hashtable(table_size)
    quadratic = Hashtable(table_size)

    for i in range(len(set)) : 
        linear.__setitem__(set[i], 'data')
        double.double_hash(set[i], 'data')
        quadratic.quadratic_probing(set[i], 'data')
    
    probes = [(linear.probes / table_size), (double.probes / table_size), (quadratic.probes / table_size)]
    collisions = [linear.collisions, double.collisions, quadratic.collisions]


    print()
    print('Total number of Small text: ', len(english_small))
    print('Total number of Large text: ', len(english_large))
    print()
    print('Total time take to read and store data into the hash table based on the size')
    print('*****************************************************************************')
    print('Small Text')
    print("***********")
    print("200000           300000          400000")
    print('*******          *******         *******')
    print(small_hash_time)
    print()
    print('Large Text')
    print("***********")
    print("200000           300000          400000")
    print('*******          *******         *******')
    print(large_hash_time)

    print()
    print('Number of Probing')
    print('******************')
    print('Linear Probing:', probes[0])
    print('Double Probing:', probes[1])
    print('Quadratic Probing:', probes[2])
    print()
    print('Number of Collisions')
    print('******************')
    print('Linear Probing:', collisions[0])
    print('Double Probing:', collisions[1])
    print('Quadratic Probing:', collisions[2])
 

