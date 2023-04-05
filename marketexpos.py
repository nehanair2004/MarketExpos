import math
import mysql.connector

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

cursor = mydb.cursor()
write_cursor = mydb_write.cursor()
cursor.execute("USE trial")


def intrinsic_value(eps, g, Y):
    earningsPerShare = eps
    growthRate = g
    bondYield = Y

    intrinsicValue = (earningsPerShare * (8.5 + 2 * growthRate) * 4.4) / bondYield
    return intrinsicValue


def margin_of_safety(V, cmp):
    intrinsicValue = V
    currentMarketPrice = cmp
    marginOfSafety = ((intrinsicValue - currentMarketPrice) / intrinsicValue) * 100

    return marginOfSafety


cf1 = []


def discounted_cashflow(cf2, r):
    cashFlow = cf2
    rate = r
    i = 1
    discountedCashFlow = 0
    for x in range(cashFlow):
        discountedCashFlow = discountedCashFlow + (cashFlow[x] / (1 + rate) ** i)

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
    bookValuePerShare = bvps

    grahamNumber = math.sqrt(22.5 * earningsPerShare * bookValuePerShare)

    return grahamNumber


cursor.execute("SELECT * FROM intrinsicvalue")  # selecting values from the intrinsic values table

for x in cursor:
    eps, g, Y, IV, cmpid = x
    IV = intrinsic_value(int(eps), int(g), float(Y))
    print(IV)
    write_cursor.execute("UPDATE intrinsicvalue SET IV = " + str(IV) + " WHERE cmpid = " + str(cmpid))
    mydb_write.commit()


intrinsicValueArr = []
discountedCashFlowArr = []
fairValueArr = []
grahamNumberArr = []

cursor.execute("SELECT cmpid,IV FROM intrinsicvalue")

for x in cursor:
    intrinsicValueArr.append(x)

# sorting
length = len(intrinsicValueArr)

for x in range(length):
    for y in range(0, length-x-1):
        tuple1 = intrinsicValueArr[y]
        tuple2 = intrinsicValueArr[y+1]
        if tuple1[1] > tuple2[1]:
            intrinsicValueArr[y], intrinsicValueArr[y+1] = intrinsicValueArr[y+1], intrinsicValueArr[y]


print(intrinsicValueArr)