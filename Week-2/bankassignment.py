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

#Formulae gross_income=net_income + taxe

net_income=int(input("Enter your net income:"))

#above 300k
if (net_income>=300000):
    gross_income=-net_income + ((30/100)*net_income)
    print("Since your net income is{} your gross income is{}".format(net_income,int(gross_income)))

#150k to less than 300k
if (net_income>=150000) & (net_income <300000):
    gross_income=net_income +((19/100)*net_income)
    print("Since your income is {} your gross income {}".format(net_income,int(gross_income)))


if(net_income >= 1) & (net_income < 100000):
	gross_income = net_income + ((5/100)*net_income)
	print("Since Your Net income is {} your Gross income is {}".format(net_income, int(gross_income)))

