import datetime , random , string

from msilib.schema import Error
from random import randint
from time import time

class Hashtable:
    def __init__(self, size):
        self.total_elements = 0
        self.size = size
        self.probes = 0
        self.collisions = 0
        self.table = [[] for _ in range(size)]


    def __getitem__(self,key):
        count = 0
        hash_key = self.hash(key)
        while(count<=self.size):
            if(self.table[hash_key]!=[] and self.table[hash_key][0] == key):
                return self.table[hash_key][1]
            else:
                hash_key = (hash_key + 1) % self.size
                count += 1
                self.probes += 1
        raise KeyError()

    def __setitem__(self,key,value):
        count = 0
        hash_key = self.hash(key)
        if(self.table[hash_key] == []):
            self.total_elements += 1
            self.table[hash_key] = [key,value]

        elif(self.table[hash_key][0]==key):
                self.table[hash_key] = [key,value]

        else:
            while(self.table[hash_key] != []):
                self.probes += 1
                hash_key = (hash_key + 1) % self.size
                count += 1
                if(count >= self.size):
                    self.collisions += 1
                    return
            self.table[hash_key] = [key,value]


    def __contains__(self,key):
        hash_key = self.hash(key)
        count = 0
        if(hash_key>=self.size):
            return False
        else:
            while(count<=self.size):
                if(self.table[hash_key] != [] and self.table[hash_key][0]==key):
                    return True
                else:
                    hash_key = (hash_key + 1) % self.size
                    count += 1
            return False

    def hash(self,key):
        return hash(str(key)) % self.size

    def double_hash(self,key,value):
        count = 0
        hash_key = self.hash(key)
        if(self.table[hash_key] == []):
            self.total_elements += 1
            self.table[hash_key] = [key,value]

        elif(self.table[hash_key][0]==key):
                self.table[hash_key] = [key,value]

        else:
            self.collisions += 1
            while(self.table[hash_key] != []):
                #find an empty slot in entire table
                hash_key = (hash_key + count*self.hash(hash_key)) % self.size
                self.probes += 1
                count += 1
                if(count >= self.size):
                    return
            self.table[hash_key] = [key,value]
            
    def quadratic_probing(self,key,value):
        count = 0
        hash_key = self.hash(key)
        if(self.table[hash_key] == []):
            self.total_elements += 1
            self.table[hash_key] = [key,value]

        elif(self.table[hash_key][0]==key):
                self.table[hash_key] = [key,value]

        else:
            self.collisions += 1
            while(self.table[hash_key] != []):
                hash_key = (hash_key + count*count) % self.size
                self.probes += 1
                count += 1
                if(count >= self.size):
                    return
            self.table[hash_key] = [key,value]

