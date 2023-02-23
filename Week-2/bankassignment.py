#/usr/bin/env python3
#Python program to calculate gross income
#Name:Isaac Thuo
#Email:zackthyru@gmail.com
#Date:17th Feb 2023
#file:bank.py

#Write a program that calculates
#16% if tax income is ranging between 100k-150k
#19% if tax income is ranging between 150k-300k
#30% if tax income is above 300k
#5% if income is less than 100k

#Formulae net_income=gross_income - taxes

#above 300k

gross_income=int (input("what is your gross income:"))
taxgroup_a=(gross_income*5/100)
taxgroup_b=(gross_income*16/100)
taxgroup_c=(gross_income*19/100)
taxgroup_d=(gross_income*30/100)

if gross_income <100000:
    print("gross_income",gross_income)
    print("net_income",gross_income-taxgroup_a)


elif (gross_income >=100001) & (gross_income <150000):
      print("gross_income",gross_income)
      print("net_income",gross_income-taxgroup_b)

elif(gross_income>=150001) & (gross_income<300000):
     print("gross_income",gross_income)
     print("net_income",gross_income-taxgroup_c)

elif(gross_income>=300001):
     print("gross_income",gross_income)
     print("net_income",gross_income-taxgroup_d)
     







      

     
