import math

import sub as sub


def intrinsic_value(eps, g, Y):
    earningsPerShare = eps
    growthRate = g
    bondYield = Y

    intrinsicValue = (earningsPerShare * (8.5 + 2 * growthRate) * 4.4) / bondYield
    return intrinsicValue


def margin_of_safety(V, cmp):
    intrinsicValue = V
    currentMarketPrice = cmp
    marginOfSafety = (intrinsicValue - currentMarketPrice) / intrinsicValue

    return marginOfSafety


cf1 = []


def discounted_cashflow(cf2, r):
    cashFlow = cf2
    rate = r
    i = 1
    discountedCashFlow = 0
    for x in range(cashFlow):
        discountedCashFlow = discountedCashFlow + (x / (1 + rate) ** i)

    return discountedCashFlow


def fair_value(c, r, x, div):
    cash = c
    rate = r
    noOfDaysLeft = x
    dividends = div

    fairValue = cash * (1 + rate * (noOfDaysLeft / 360)) - dividends

    return fairValue


def graham_number(eps, bvps):
    earningsPerShare = eps
    bookvaluePerShare = bvps

    grahamNumber = math.sqrt(22.5 * earningsPerShare * bookvaluePerShare)

    return grahamNumber


print(intrinsic_value(23, 10, 3.7))

import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Padfootmay2",
    db="trial")

mydb_write = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Padfootmay2",
    db="trial")
# Printing the connection object
print(mydb)
print(mydb_write)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()
write_cursor = mydb_write.cursor()

cursor.execute("USE trial")  # open trial table

eps = 0
g = 0
Y = 0
IV = 0
cmpid = 0

cursor.execute("SELECT * FROM intrinsicvalue")  # selecting values from the intrinsic values table

for x in cursor:
    eps, g, Y, IV, cmpid = x
    IV = intrinsic_value(int(eps), int(g), float(Y))
    print(IV)
    write_cursor.execute("UPDATE intrinsicvalue SET IV = " + str(IV) + " WHERE cmpid = " + str(cmpid))
    mydb_write.commit()
