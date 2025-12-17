from functools import cache
import customtkinter as ctk 
import csv 
import os
from datetime import datetime




class other:
    def common(list1, list2):
        com = list(set(list1) & set(list2))   
        return com
    def map(list1,list2):
        set1 = set(list1)
        set2 = set(list2)
        if len(set1) >= len(set2):
            diff = set1 - set2
            return len(diff)
        else:
            diff = set2 - set1
            return len(diff)
    def cache(user):
        global cache
        cache = None  # Initialize cache
        if not os.path.exists("users.csv"):
            with open("users.csv","w") as file:
                pass
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and len(row) > 0 and row[0] == user:
                    cache = row 
                    return cache
