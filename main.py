# Imports
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.
def main():
    pass

#argparse function

    parser = argparse.ArgumentParser(description="my supemarket")
    parser.add_argument("product", metavar="product", type=str, help="find your product")
    args = parser.parse_args()
    product = args.product
    # inventory
    inventory_parser = subparsers.add_parser("buy", help="bought product")
    inventory_parser.add_argument("item", action="store", help="New product")
    inventory_parser.add_argument("--read-only",type=datetime.date.isoformat,action="store_true",help="Set date time",)
    # sell
    sell_parser = subparsers.add_parser("sold", help="Remove product")
    sell_parser.add_argument("item", action="store", help="The product to remove")
    sell_parser.add_argument("--recursive","-r",default=False,action="store_true",help="Remove the items",)

    print(args.sum(args.product))
    

#making the file inventory.csv 


def csv_inventory():
    csv_columns = ["product","count","price",]
    dict_data = [
        {"product": "apple", "count": 16, "price": 1},
        {"product": "coffee", "count": 23, "price": 2},
        {"product": "chicken", "count": 43, "price": 4},
        {"product": "yoghurt", "count": 22, "price": 2},
        {"product": "coca cola", "count": 60, "price": 3},
        ]
    csv_file = "Inventory.csv"
    try:
        with open(csv_file, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter="\t")
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


#making the file sold.csv 


def csv_sold():
     fieldnames = ["bought_id", "sell_date", "sell_price"]
     rows = [
         {"product": "apple", "count": 16, "price": 1},
         {"product": "coffee", "count": 23, "price": 2},
         {"product": "chicken", "count": 43, "price": 4},
         {"product": "yoghurt", "count": 22, "price": 2},
         {"product": "cheese", "count": 52, "price": 3},
         {"product": "coca cola", "count": 60, "price": 3},
         {"product": "broccoli", "count": 32, "price": 2},
         {"product": "milk", "count": 43, "price": 2},
         ]
     csv_file = "sold.csv"
     with open("sold.csv", "w", newline="") as csvfile:
         writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=" ")
         writer.writeheader()
         for rows in writer:
             writer.writerows(rows)
             print(rows)
             sell_data = csv_data("sold.csv")
             return sell_data

#buying the products

def buy_function(store_list, product_name, buy_price):
    store_data = [
        {"product": "apple", "count": 16, "price": 1},
        {"product": "coffee", "count": 23, "price": 2},
        {"product": "chicken", "count": 43, "price": 4},
        {"product": "yoghurt", "count": 22, "price": 2},
        {"product": "coca cola", "count": 60, "price": 3},
        ]
    with open("sold.csv", "a", newline="") as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
        for product in store_data:
            writer.writerow(product)
            if args.command == "sold":
                product = args.product
                (product["product_name"] == product_name
                 and product["price"] == buy_price
                 and product['count'] == store_list)
                item_index = index
                if item_index == -1:
                        buy_data.append(
                            {   "Product Name": product_name,
                                "Count": count,
                                "Buy Price": buy_price,
                                "Expiration Date": expiration_date,})
                        return buy_data


def advance_time():
    if args.command == "date":
        new_day = (datetime.datetime.today() + datetime.timedelta(days=n)).strftime("%Y-%m-%d")
        global today
        today = new_day  # overwrite today with new_day
        print("OK")
        

csv_inventory()
advance_time()
buy_function()
csv_sold()

       
                
                
        
if __name__ == '__main__':
    main()
