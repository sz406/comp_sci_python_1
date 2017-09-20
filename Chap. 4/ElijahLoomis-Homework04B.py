#Elijah-Homework04B.py
#Elijah Loomis
#This program charts the sales of individual stores

import sys

print("Elijah loomi's Store Sales")
print("\n")

#Store input
store_1 = int(input("Enter todays sales for store 1: "))
store_2 = int(input("Enter todays sales for store 2: "))
store_3 = int(input("Enter todays sales for store 3: "))
store_4 = int(input("Enter todays sales for store 4: "))
store_5 = int(input("Enter todays sales for store 5: "))

#print(store_1)

#Number convert
store_1 = store_1 / 100
store_2 = store_2 / 100
store_3 = store_3 / 100
store_4 = store_4 / 100
store_5 = store_5 / 100

#Float to int convert
store_1 = int(store_1)
store_2 = int(store_2)
store_3 = int(store_3)
store_4 = int(store_4)
store_5 = int(store_5)

#Chart Convert
chart = '*'

chart1 = chart * store_1
chart2 = chart * store_2
chart3 = chart * store_3
chart4 = chart * store_4
chart5 = chart * store_5

#Print Charts
print("\n")
print("SALES BAR CHARTS")
print("(Each * = $100)")

print("Store 1:", chart1)
print("Store 2:", chart2)
print("Store 3:", chart3)
print("Store 4:", chart4)
print("Store 5:", chart5)

#Exit
print("\n")
exit = input("Exit? y/n:")
if exit == "y":
    sys.exit(1)

