import csv
import random
from datetime import datetime, timedelta
import pandas as pd

def get_user_inputs():
    """Get user inputs for bill generation"""
    print("=== Bill Generator ===")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    number_of_bills = int(input("Enter number of bills to generate: "))
    total_bill_amount = float(input("Enter total bill amount target: "))
    products_csv = input("Enter products CSV file path (default: products.csv): ") or "products.csv"
    
    return start_date, end_date, number_of_bills, total_bill_amount, products_csv

def load_products(products_csv):
    """Load products from CSV file"""
    products = []
    print(f"Attempting to load products from: {products_csv}")
    try:
        with open(products_csv, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            print(f"CSV reader fieldnames: {reader.fieldnames}")
            row_count = 0
            for row in reader:
                row_count += 1
                # Handle both BOM and non-BOM column names
                product_name_key = None
                product_price_key = None
                
                for key in row.keys():
                    if key.replace('ï»¿', '') == 'Product_Name':
                        product_name_key = key
                    elif key.replace('ï»¿', '') == 'Product_Price':
                        product_price_key = key
                
                if not product_name_key or not product_price_key:
                    print(f"Skipping row {row_count}: Missing columns")
                    continue
                
                product_name = row[product_name_key].strip()
                product_price = row[product_price_key].strip()
                
                # Skip empty product names or prices
                if product_name and product_price:
                    try:
                        products.append({
                            'name': product_name,
                            'price': float(product_price)
                        })
                        print(f"Loaded product: {product_name} - ${product_price}")
                    except ValueError:
                        # Skip rows with invalid price values
                        print(f"Skipping row {row_count}: Invalid price '{product_price}'")
                        continue
                else:
                    print(f"Skipping row {row_count}: Empty name or price")
            
            print(f"Total rows processed: {row_count}")
            print(f"Total products loaded: {len(products)}")
    except FileNotFoundError:
        print(f"Error: Products file '{products_csv}' not found.")
        return []
    except Exception as e:
        print(f"Error reading products file: {e}")
        return []
    
    return products

def generate_random_date(start_date, end_date):
    """Generate a random date between start_date and end_date"""
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    delta = end - start
    random_days = random.randint(0, delta.days)
    random_date = start + timedelta(days=random_days)
    
    return random_date.strftime("%Y-%m-%d")

def generate_single_bill(bill_id, start_date, end_date, products):
    """Generate a single bill with random products"""
    bill_date = generate_random_date(start_date, end_date)
    
    # Generate random products for this bill
    bill_products = []
    current_total = 0
    
    # Select random number of products (between 1 and 8)
    num_products = random.randint(1, min(8, len(products)))
    selected_products = random.sample(products, num_products)
    
    for product in selected_products:
        # Random quantity for each product (between 1 and 5)
        quantity = random.randint(1, 3)
        product_total = product['price'] * quantity
        
        bill_products.append({
            'product_name': product['name'],
            'quantity': quantity,
            'unit_price': product['price'],
            'total_price': product_total
        })
        
        current_total += product_total
    
    # Use the actual calculated total without adjustment
    final_total = current_total
    
    return {
        'bill_id': bill_id,
        'bill_date': bill_date,
        'products': bill_products,
        'total_amount': round(final_total, 2)
    }

def generate_bills(start_date, end_date, number_of_bills, total_bill_amount, products_csv):
    """Generate multiple bills"""
    products = load_products(products_csv)
    
    if not products:
        print("No products loaded. Cannot generate bills.")
        return []
    
    bills = []
    
    for i in range(1, number_of_bills + 1):
        bill = generate_single_bill(i, start_date, end_date, products)
        bills.append(bill)
        print(f"Generated Bill {i}: {bill['bill_date']} - ${bill['total_amount']}")
    
    # Check tolerance
    total_generated = sum(bill['total_amount'] for bill in bills)
    tolerance_percent = ((total_generated - total_bill_amount) / total_bill_amount) * 100
    
    print(f"\nTarget amount: ${total_bill_amount:.2f}")
    print(f"Generated amount: ${total_generated:.2f}")
    print(f"Tolerance: {tolerance_percent:.2f}%")
    
    if abs(tolerance_percent) <= 20:
        print("Within ±20% tolerance - ACCEPTABLE")
    else:
        print("Outside ±20% tolerance - You may want to regenerate")
    
    return bills

def export_bills_to_csv(bills, output_filename="generated_bills.csv"):
    """Export bills to CSV file"""
    with open(output_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Bill_ID', 'Bill_Date', 'Product_Name', 'Quantity', 'Unit_Price', 'Total_Price', 'Bill_Total'])
        
        # Write bill data
        for bill in bills:
            for product in bill['products']:
                writer.writerow([
                    bill['bill_id'],
                    bill['bill_date'],
                    product['product_name'],
                    product['quantity'],
                    product['unit_price'],
                    product['total_price'],
                    bill['total_amount']
                ])
    
    print(f"\nBills exported to '{output_filename}'")
    print(f"Total bills generated: {len(bills)}")
    total_generated = sum(bill['total_amount'] for bill in bills)
    print(f"Total amount generated: ${total_generated:.2f}")

def main():
    """Main function to run the bill generator"""
    try:
        # Get user inputs
        start_date, end_date, number_of_bills, total_bill_amount, products_csv = get_user_inputs()
        
        # Validate date format
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        
        if number_of_bills <= 0 or total_bill_amount <= 0:
            print("Number of bills and total bill amount must be positive.")
            return
        
        # Generate bills
        print(f"\nGenerating {number_of_bills} bills...")
        bills = generate_bills(start_date, end_date, number_of_bills, total_bill_amount, products_csv)
        
        if bills:
            # Export to CSV
            export_bills_to_csv(bills)
            
            # Show sample of first bill
            print(f"\n=== Sample Bill (Bill ID: {bills[0]['bill_id']}) ===")
            print(f"Date: {bills[0]['bill_date']}")
            print(f"Products:")
            for product in bills[0]['products']:
                print(f"  - {product['product_name']}: {product['quantity']} x ${product['unit_price']} = ${product['total_price']}")
            print(f"Total: ${bills[0]['total_amount']}")
        
    except ValueError as e:
        print(f"Error: Invalid input format. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()