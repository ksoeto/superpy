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
    
    def write_to_csv(dict):
    with open('inventory.csv', 'w', newline='') as csvfile:
        fieldnames = ['product_name', 'count', 'buy_price', 'expiration_date']
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        

    d = datetime.date(2021, 5, 4)



if __name__ == '__main__':
    main()
