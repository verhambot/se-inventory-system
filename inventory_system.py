import ast
import json
import logging
from datetime import datetime

# BUGFIX 3
logs = []


def addItem(stock_data, item="default", qty=0):
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))


def removeItem(stock_data, item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # BUGFIX 2
    except KeyError:
        print(f"Key {item} not found in stock_data.")


def getQty(stock_data, item):
    return stock_data[item]


def loadData(file="inventory.json"):
    f = open(file, "r")
    stock_data = json.loads(f.read())
    f.close()
    return stock_data


def saveData(stock_data, file="inventory.json"):
    f = open(file, "w")
    f.write(json.dumps(stock_data))
    f.close()


def printData(stock_data):
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def checkLowItems(stock_data, threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():

    # BUGFIX 4
    stock_data = {}

    addItem(stock_data, "apple", 10)
    addItem(stock_data, "banana", -2)
    addItem(stock_data, 123, "ten")  # invalid types, no check
    removeItem(stock_data, "apple", 3)
    removeItem(stock_data, "orange", 1)
    print("Apple stock:", getQty(stock_data, "apple"))
    print("Low items:", checkLowItems(stock_data))
    saveData(stock_data)
    stock_data = loadData()
    printData(stock_data)

    # BUGFIX 1
    ast.literal_eval("print('eval used')")


main()
