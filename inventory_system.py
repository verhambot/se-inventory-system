import ast
import json
# BUGFIX 9: removed logging import
from datetime import datetime

# BUGFIX 3
logs = []


def add_item(stock_data, item="default", qty=0):
    # BUGFIX 11
    if (not item) or (not isinstance(item, str)) or (not isinstance(qty, (int, float))):
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    # BUGFIX 10
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def remove_item(stock_data, item, qty):
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # BUGFIX 2
    except KeyError:
        print(f"Key {item} not found in stock_data.")


def get_qty(stock_data, item):
    return stock_data[item]


def load_data(file="inventory.json"):
    # BUGFIX 5 & 6
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.loads(f.read())
    return stock_data


def save_data(stock_data, file="inventory.json"):
    # BUGFIX 7 & 8
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


def print_data(stock_data):
    print("Items Report")
    for i in stock_data:
        print(i, "->", stock_data[i])


def check_low_items(stock_data, threshold=5):
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result


def main():

    # BUGFIX 4
    stock_data = {}

    add_item(stock_data, "apple", 10)
    add_item(stock_data, "banana", -2)
    add_item(stock_data, 123, "ten")
    remove_item(stock_data, "apple", 3)
    remove_item(stock_data, "orange", 1)
    print("Apple stock:", get_qty(stock_data, "apple"))
    print("Low items:", check_low_items(stock_data))
    save_data(stock_data)
    stock_data = load_data()
    print_data(stock_data)

    # BUGFIX 1
    ast.literal_eval("print('eval used')")


main()
