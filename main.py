# Imports
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.
def main():

    #argparse function 
    parser= argparse.ArgumentParser(description="My supermarket")
    subparsers=parser.add_subparsers(dest="command")
    parser.add_argument("-s", help="open the user inventory")

    
    # inventory
    inventory_parser = subparsers.add_parser("buy", help="bought product")
    inventory_parser.add_argument('--price', action="store", help=" new item")
    inventory_parser.add_argument('--product', type=str, metavar='', required = True, help='Enter name of the bought product')
    inventory_parser.add_argument('--expiration-date',type= datetime.date.fromisoformat,help="insert date as: YYYY-MM-DD",)
    #  sell
    sell_parser = subparsers.add_parser("sold", help="Remove product")
    sell_parser.add_argument("item", action="store", help="The product to remove")
    sell_parser.add_argument("--recursive","-r",default=False,action="store_true",help="Remove the items",)

    #report parser
    search_parser = subparsers.add_parser("report", help="report transactions")    
    search_parser.add_argument("option",action='store_true', help="show current inventory")
    search_parser.add_argument("--yesterday", action="store_true", help="show yesterday's inventory")
    

    args = parser.parse_args()
    
    return args  

def csv_inventory():
    with open("inventory.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter="\t")
        inventory_file = csv.writer(csvfile)
        inventory_file.writerow(['product_name', 'buy_price', 'expiration_date']) 

def buy_function():
    lines = 0
    item_index = lines
    product = args.product
    buy_price = args.price
    expiration_date = args.expiration_date
    with open("inventory.csv", "r",newline = '') as csvfile: 
        reader = csv.reader(csvfile)
        for row in reader:
                lines += 1
    with open('inventory.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)

            row= [
                    item_index, 
                    args.product,
                    args.price, 
                    args.expirationdate,
                ]
            writer.writerow(row) 
    with open('inventory.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            list_ids = []
            for row in reader:
                if args.product in row:
                    if datetime.datetime.strptime(self.get_date(), '%Y-%m-%d %H:%M:%S') < datetime.datetime.strptime((row[4]), '%Y-%m-%d'):
                        list_ids.append(row[0]) 
        
#selling function 

def sell_function(product_name, sell_price):
    lines = 0
    with open('sold.csv','r',newline="") as csvfile:
         reader = csv.reader(csvfile)
         for row in reader:
             lines += 1
             sold_item = []
    with open('sold.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            sold_item.append(row[1])
    with open('inventory.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        sell_data = []
        for row in reader:
            if args.prodname in row:
                sell_data.append(row[0])

def sold_product(date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    sold_list = []
    with open('sold.csv', 'r') as csv_file:
        for line in csv_file:
            if "product_id" in line:
                continue
            line = line[:-1]
            sell_date = line.split(",")[3]
            sell_date2 = dt.datetime.strptime(sell_date, "%Y-%m-%d").date()

            if sell_date2 <= date:
                sold_list.append(line.split(","))

    return sold_list


def advance_time():
    if args.advance_time:
        expiration_date = datetime.date.fromisoformat
        new_day = (datetime.datetime.today() + datetime.timedelta(days=n)).strftime("%Y-%m-%d")
        today = new_day  # overwrite today with new_day
                 
            
if __name__ == '__main__':
    args = main()
    csv_inventory()
    buy_function(args)
    sell_function()
