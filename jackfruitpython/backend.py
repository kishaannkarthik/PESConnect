from functools import cache
import customtkinter as ctk 
import csv 
import os
from datetime import datetime
from other import other





class backend:
    def metro(user,course1= None, value = True):
         g1= ["Nagasandra", "Dasarahalli", "Jalahalli", "Peenya Industry", "Peenya", "Goraguntepalya",
         "Yeshwanthpur", "Sandal Soap Factory", "Mahalakshmi", "Rajajinagar", "Kuvempu Road",
         "Srirampura", "Mantri Square Sampige Road"]
         g2 = ["Chickpet",    "Krishna Rajendra Market",    "National College",    "Lalbagh Botanical Garden",
         "South End Circle",    "Jayanagar",    "R.V. Road",    "Banashankari",    "Rashtreeya Vidyalaya Road",  
         "J.P. Nagar",    "Yelachenahalli","Konanakunte Cross","Doddakallasandra","Silk Institute"]
         g2 = g2[::-1]
         p1 = ["Whitefield (Kadugodi)", "Hopefarm Channasandra", "Kadugodi Tree Park", "Pattanduru Agrahara",
          "Sri Sathya Sai Hospital", "Nallurhalli", "Kundalahalli", "Seetharamapalya", "Hoodi",
         "Garudacharpalya", "Mahadevapura", "K.R. Puram", "Benniganahalli", "Baiyappanahalli",
         "Swami Vivekananda Road", "Indiranagar", "Halasuru", "Trinity", "M.G. Road", "Cubbon Park",
          "Vidhana Soudha", "Sir M. Visvesvaraya Station", "Nadaprabhu Kempegowda Station (Majestic)",
          "City Railway Station", "Magadi Road", "Hosahalli", "Vijayanagar", "Attiguppe",
          "Deepanjali Nagar"]
         p2= ["Nayandahalli", "Rajarajeshwari Nagar", "Jnanabharathi",
          "Pattanagere", "Kengeri", "Kengeri Bus Terminal", "Challaghatta"]
         p2 = p2[::-1]
         g1_p = g1 + p1[22::]
         g2_p = g2 + p1[22::]
         with open('users.csv', mode='r') as file: 
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 2 and row[0] == user:
                   userlist = row[2].split("#")
                   if any(station in g1 + g2 + p1 + p2 for station in userlist):
                       spot = other.common(userlist, g1)
                       return [None, spot] 
                   elif not value:
                       if any(station in g1 for station in userlist):
                           spot = other.common(userlist, g1)
                           if spot:
                               ind = g1.index(spot[0])
                               course  = g1_p[ind::]
                               diff = other.map(course, course1)
                               if diff <=3 or course1 == None:
                                   return [course,spot]
                       elif any(station in g2 for station in userlist):
                           spot = other.common(userlist, g2)
                           if spot:
                               ind = g2.index(spot[0])
                               course  = g2_p[ind::]
                               diff = other.map(course, course1)
                               if diff <=3 or course1 == None:
                                   return [course,spot]
                       elif any(station in p1 for station in userlist):
                           spot = other.common(userlist, p1)
                           if spot:
                               ind = p1.index(spot[0])
                               course  = p1[ind::]
                               diff = other.map(course, course1)
                               if diff <=3 or course1 == None:
                                   return [course,spot]
                       elif any(station in p2 for station in userlist):
                           spot = other.common(userlist, p2)
                           if spot:
                               ind = p2.index(spot[0])
                               course  = p2[ind::]
                               diff = other.map(course, course1)
                               if diff <=3 or course1 == None:
                                   return [course,spot]
            return []
    def sports(user):
        global sports
        sports = ["Basketball", "Batminton","Squash","Gym","Volleyball","Table Tennis","Kabaddi"]
        with open('users.csv', mode='r') as file: 
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 3 and row[0] == user:
                    if any(sport in sports for sport in row[3].split('#')):
                        com = other.common(row[3].split("#"), sports)
                        return com
        return []
    
    def study(user):
        global course
        course = ["ECE","CSE","MECH","CIVIL","BBA","MBA","MCA","LAW","DESIGN","BCA"]
        with open('users.csv', mode='r') as file: 
            reader = csv.reader(file)
            for row in reader:
                if len(row) > 4 and row[0] == user:
                    if any(c in course for c in row[4].split('#')):
                        com = other.common(row[4].split("#"), course)
                        return com
        return []
