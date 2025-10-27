import ast
import json
# BUGFIX 9: removed logging import
from datetime import datetime

# BUGFIX 3
logs = []


def addItem(stock_data, item="default", qty=0):
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # BUGFIX 10
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


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
    # BUGFIX 5 & 6
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())
    return stock_data


def saveData(stock_data, file="inventory.json"):
    # BUGFIX 7 & 8
    with open(file, "r", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


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
