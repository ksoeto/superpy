# Imports
import argparse 
import csv
import datetime  
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.
def main():


    # argparse function 
    parser = argparse.ArgumentParser(description="My supermarket")
    subparsers = parser.add_subparsers(dest="command")
    parser.add_argument('-t', '--advance_time', type=int, help='Advance time. Please specify the number of days with this argument')
    parser.add_argument('-o', '--open_interface', action='store_true', help='Open the user interface')

    # Buy
    buy_parser = subparsers.add_parser("buy", help="buy a product")
    buy_parser.add_argument('--product_name', type=str, required=True, help='Enter name of the bought product')
    buy_parser.add_argument('--price', action="store", help="new item")
    buy_parser.add_argument('--product', type=str, required=True, help='Enter name of the bought product')
    buy_parser.add_argument('--buy_date', type=str, help='Enter buy date of the bought product in YYYY-mm-dd format')

    # Sell
    sell_parser = subparsers.add_parser("sell", help='Sell an item')
    sell_parser.add_argument('--product_name', type=str, help='Enter name of the sold product')
    sell_parser.add_argument('--price', type=float, required=True, help='Enter price of the sold product')

    # Inventory parser
    inventory_parsers = subparsers.add_parser(help='Show current inventory')
    inventory_parsers = inventory_parsers.add_subparsers(help='What kind of report would you like?')
    inventory_revenue = inventory_parsers.add_parser('inventory', help='Show inventory')
    inventory_profit = inventory_parsers.add_parser('profit', help='Calculate profit')

    inventory_parsers.add_argument('--now', action='store_true', help='Show current inventory')
    inventory_parsers.add_argument('--yesterday', action='store_true', help='Show yesterday\'s inventory')
    inventory_parsers.add_argument('--date', type=str, help='Show inventory on date using YYYY-mm-dd format')
    inventory_revenue.add_argument('--today', action='store_true', help='Show today\'s revenue')
    inventory_revenue.add_argument('--yesterday', action='store_true', help='Show yesterday\'s revenue')
    inventory_revenue.add_argument('--date', type=str, help='Show revenue on a specific date using YYYY-mm-dd format')
    inventory_revenue.add_argument('--period', type=str, help='Show revenue for a specific period (YYYY-mm-dd/YYYY
    
    return args  

def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

#The function used to advance the date stored as 'today'.
#Takes the current date and adds the specified number of days.
def advance_time(days):
    current_date = datetime.datetime.now()
    new_date = current_date + datetime.timedelta(days=days)
    with open('date.csv', 'w') as date_file:
        writer = csv.writer(date_file)
        writer.writerow([new_date.strftime('%Y-%m-%d')])

#The main action for buying a product. Requires a name, price, expiration date and date of purchase
#Generates a new ID based on the last know ID and stores all values in a csv file.
def buy_item(product_name, buy_price, expiration_date, buy_date='today'):
    """
    Add a bought item to the bought_items.csv file
    """
    product_name = product_name.lower()
    # Open the CSV file in r+ mode to read and append new rows
    with open('bought_items.csv', 'r+', newline='') as file:
        reader = csv.reader(file)
        # Find the highest buy ID in the file to assign a new one
        find_buy_id = [0]
        for row in reader:
            bought_id = int(row[0])
            find_buy_id.append(bought_id)
        bought_id = max(find_buy_id) + 1
        # If buy_date isn't specified, use today's date
        if buy_date == 'today':
            date_bought = datetime.date.today().strftime('%Y-%m-%d')
        else:
            date_bought = buy_date
        # Write the new bought item to the file
        writer = csv.writer(file)
        writer.writerow([bought_id, product_name, date_bought, buy_price, expiration_date])
        print(f"{product_name.capitalize()} bought for {buy_price} on {date_bought} (expires on {expiration_date})")

#The main action for selling a product. Requires a name and price and stores these values with the Buy-ID in a csv file. 
def sell_item(product_name, sell_price):
    date = get_date()
    with open('sold.csv', 'r+', newline='') as sold_file:
        sold_reader = csv.reader(sold_file)
        next(sold_reader)
        sold_items_list = []
        for line in sold_reader:
            sold_items_list.append(line[1])
        find_sold_id = [0]
        sold_file.seek(0)
        next(sold_reader)
        for row in sold_reader:
            sold_id = int(row[0])
            find_sold_id.append(sold_id)
        sold_id = max(find_sold_id) + 1
    with open('bought.csv', newline='') as bought_file:
        bought_reader = csv.reader(bought_file)
        next(bought_reader)
        stock = []
        for line in bought_reader:
            if line[1] == product_name and datetime.datetime.strptime(line[4], "%Y-%m-%d").date() >= date and line[0] not in sold_items_list:
                stock.append(line[0])
        if stock:
            bought_id = stock[0]
            with open('sold.csv', 'a', newline='') as sold_file:
                sold_item = csv.writer(sold_file)
                sold_item.writerow([sold_id, bought_id, date, sell_price])
        else:
            print('Item not in stock')


def check_inventory(time):
    with open('sold.csv', 'r+', newline='') as sold_file:
        sold_reader = csv.reader(sold_file)
        next(sold_reader)
        sold_items_list = []
        for line in sold_reader:
            if datetime.datetime.strptime(line[2], "%Y-%m-%d").date() <= time:
                sold_items_list.append(line[1])
    with open('bought.csv', newline='') as bought_file:
        bought_reader = csv.reader(bought_file)
        next(bought_reader)
        stock = []
        for line in bought_reader:
            if datetime.datetime.strptime(line[4], "%Y-%m-%d").date() > time and line[0] not in sold_items_list and datetime.datetime.strptime(line[2], "%Y-%m-%d").date() <= time:
                stock.append([line[1].lower(), line[3], line[4]])
        unique_stock = []
        for i in stock:
            if i not in unique_stock:
                unique_stock.append(i)
                unique_stock = sorted(unique_stock)
        fields = ['Product name', 'Count', 'Buy Price', 'Expiration Date']
        with open(f'Inventory {time}.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(unique_stock)
        inventory = f'Inventory saved as Inventory {time}.csv \nProduct name \tCount \tBuy Price \tExpiration Date'
        for row in unique_stock:
            inventory = inventory + f'\n{row[0]} \t\t{stock.count(row)} \t{row[1]} \t\t{row[2]}'
        print(inventory)
        return inventory


def profit(start_date, end_date):
    profit = 0
    with open('sold.csv', 'r') as sold_file:
        sold_reader = csv.reader(sold_file)
        next(sold_reader)  
        for row in sold_reader:
            sold_date = datetime.datetime.strptime(row[2], '%Y-%m-%d')
            if sold_date >= start_date and sold_date <= end_date:
                cost = float(row[1])
                with open('purchased.csv', 'r') as purchased_file:
                    purchased_reader = csv.reader(purchased_file)
                    next(purchased_reader)
                    for item in purchased_reader:
                        if item[0] == row[0] and datetime.datetime.strptime(item[3], '%Y-%m-%d') <= sold_date:
                            cost = float(item[1])
                profit += (float(row[1]) - cost)
    return profit

def revenue_period(start_date, end_date):
    revenue = 0
    with open('sold.csv', 'r') as sold_file:
        sold_reader = csv.reader(sold_file)
        next(sold_reader)  
        for row in sold_reader:
            sold_date = datetime.datetime.strptime(row[2], '%Y-%m-%d')
            if sold_date >= start_date and sold_date <= end_date:
                revenue += float(row[1])
    return revenue




    #Function used to create a list of items for sale, to help the user specify what has been sold.
    #Only items in stock and with a suitable expiration date are shown.
def create_sell_items():
    date = get_date()
    with open('sold.csv', 'r+', newline='') as sold_file:
        sold_reader = csv.reader(sold_file)
        next(sold_reader)
        sold_list = [line[1] for line in sold_reader]
    with open('bought.csv', newline='') as bought_file: 
        bought_reader = csv.reader(bought_file)
        next(bought_reader)
        stock = [line[1] for line in bought_reader if datetime.datetime.strptime(line[4], "%Y-%m-%d").date() >= date and line[0] not in sold_list] #Creates a list of all items with that product name that are not expired nor sold
        unique_stock_names =["Select item"]
        for i in stock:
            if i not in unique_stock_names:
                unique_stock_names.append(i)
        unique_stock = sorted(unique_stock_names)
    return unique_stock

#These functions are calles when one of the buttons on the main screen are pressed.

def command_buy_product(buy_name_entry, buy_price_entry, buy_cal, window): 
    product = buy_name_entry.get()
    if product == '':
        messagebox.showerror("Error", "Please provide a valid name")
        return
    price_box = buy_price_entry.get()
    if price_box == '':
        messagebox.showerror("Error", "Please provide a valid price")
        return
    price = float(price_box)
    ex_date =  buy_cal.get_date()
    buy_name_entry.delete(0,END)
    buy_price_entry.delete(0,END)
    buy_date = get_date()
    buy_item(product, price, ex_date, buy_date)
    messagebox.showerror("Bought!", f"{product} bought for {price}!")
    refresh_window(window)

def command_advance_time(date_advance_entry, window):
    interval_box = date_advance_entry.get()
    if interval_box == '':
        messagebox.showerror("Error", "Please provide a number")
        return
    interval = int(interval_box)
    advance_time(interval)
    date = get_date()
    messagebox.showinfo("Time travel!", f"Date set to {date}")
    refresh_window(window)


if __name__ == '__main__':
    args = main()
    csv_inventory()
    buy_function()
    sell_function()