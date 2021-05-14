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
    

    parser = argparse.ArgumentParser(description='my supemarket')
    parser.add_argument('product',metavar='product', type=str, help='find your product')
    args = parser.parse_args()
    product= args.product
    #inventory 
    inventory_parser = subparsers.add_parser('buy', help='bought product')
    inventory_parser.add_argument('item', action='store', help='New product')
    inventory_parser.add_argument('--read-only', type=datetime.date.isoformat, action='store_true',
                           help='Set date time',)
    #sell 
    sell_parser = subparsers.add_parser('sold', help='Remove product')
    sell_parser.add_argument('item', action='store', help='The product to remove')
    sell_parser.add_argument('--recursive', '-r', default=False, action='store_true',
                           help='Remove the items',)

    print(args.sum(args.product))

store = [{'product':'apple','count': 16,'price':1},
         {'product':'coffee','count': 23,'price':2},
         {'product':'chicken','count': 43,'price':4},
         {'product':'yoghurt','count': 22,'price':2},
         {'product':'cheese','count': 52,'price':3},
         {'product':'coca cola','count':60,'price':3},
         {'product':'broccoli','count': 32,'price':2},
         {'product':'milk','count': 43,'price':2}]

     
    

def csv_inventory(file_name):
    with open('inventory.csv', 'w', newline = '') as csvfile:
        fieldnames=[id,'product_name','buy_date','buy_price',]
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter ='\t')
        csvwriter.writeheader()
        csvwriter.writerows({'product':'apple','count': 16,'price':1})
        csvwriter.writerows({'product':'coffee','count': 23,'price':2})
        csvwriter.writerows({'product':'chicken','count': 43,'price':4})
        csvwriter.writerows({'product':'yoghurt','count': 22,'price':2})
        csvwriter.writerows({'product':'coca cola','count':60,'price':3})
        write_to_csv(inventory_data)
        for line in csvwriter:
            print(line)
            inventory_data = csv_data('inventory.csv')
        return inventory_data
        
csv_inventory(inventory-data)
        
def csv_sold():
    with open('sold.csv', 'w', newline = '') as csvfile:
        fieldnames=[id,'bought_id','sell_date','sell_price']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter ='\t')
        csvwriter.writeheader()
        csvwriter.writerows()
        write_to_csv(sell_data)
        for line in csvwriter:
            print(line)
            sell_data = csv_data('sold.csv')
        return sell_data
        
csv_sold()
    
        
def buy_function(store_list,product_name, buy_price):
        with open('inventory.csv', 'a', newline='') as csvfile:
            writer = csv.writer(bought_file)
            for inventory_data in open('inventory.csv'):
            row = [inventory_id, product_name, date, buy_price, expiration_date]
            writer.writerow(row)
            if args.command == 'buy':
                product_name = args.product
       
                
                
        
if __name__ == '__main__':
    main()
