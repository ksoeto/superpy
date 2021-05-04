# Imports
import argparse
import csv
from datetime import date

# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.
def main():
    parser = argparse.ArgumentParser(description='my supemarket')
    parser.add_argument('product',metavar='product', type=str, help='find your product')
    args = parser.parse_args()
    product= args.product
    buy = subparser.add_parser('buy', help='register bought products')
    sell = subparser.add_parser('sell', help='register sold product')
    report = subparser.add_parser('report', help='report transactions')
# Buy Parser
    buy.add_argument('-n', '--product-name', metavar='\b', help='product name')
    buy.add_argument('-p',  '--price', metavar='\b', help='price')
    buy.add_argument('-d', '--expiration-date', metavar='\b', help='expiration date')
    
    print(args.sum(args.integers))

def write_to_csv(dict):
    with open('inventory.csv', 'w', newline='') as csvfile:
        fieldnames = ['product_name', 'count', 'buy_price', 'expiration_date']
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        dict_writer.writeheader()
        dict_writer.writerows(dict)
write_to_csv(buy_data)
def load_csv_data()
data_dict_list=
with open('bought.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter =_'\t'_)
        for line in csv_reader:
            print(line)
buy_data = load_csv_data('bought.csv')
sell_data = load_csv_data('sold.csv')
def restructure_dict():
    product_name = None
    buy_price = 0
    expiration_date = datetime.date.fromisoformat
    item_index = -1
    count = 1
    if args.command == 'buy':
        product_name = args.product_name
        buy_price = args.price
        expiration_date = str(args.expiration_date)
    for product in buy_data:
        for item, index in product.items():
            if product['product_name'] == product_name and product['buy_price'] == buy_price and product['expiration_date'] == expiration_date:
                item_index = index
        if item_index == -1:
            buy_data.append({'Product Name': product_name, 'Count': count, 'Buy Price': buy_price, 'Expiration Date': expiration_date})
        else:
            product[item_index]['Count'] += count
        return buy_data




d= datetime.date(2021, 4, 11)



if __name__ == '__main__':
    main()
