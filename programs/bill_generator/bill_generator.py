import csv
import random
import os
import numpy as np
from datetime import datetime

def get_user_inputs():
    """Get user inputs for bill generation"""
    print("=== Bill Generator ===")
    print("\n--- Date Range ---")
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    
    print("\n--- Fancy Items ---")
    fancy_bills = int(input("Enter number of bills for fancy items: "))
    fancy_amount = float(input("Enter total bill amount target for fancy items: "))
    
    print("\n--- Cloths ---")
    cloths_bills = int(input("Enter number of bills for cloths: "))
    cloths_amount = float(input("Enter total bill amount target for cloths: "))
    
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    return start_date, end_date, fancy_bills, fancy_amount, cloths_bills, cloths_amount

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
                    clean_key = key.replace('ï»¿', '').replace('\ufeff', '')
                    if clean_key == 'Product_Name':
                        product_name_key = key
                    elif clean_key == 'Product_Price':
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

def generate_single_bill(bill_id, products, target_amount):
    """Generate a single bill with products that add up to target amount"""
    bill_products = []
    
    # Generate random products until we reach close to target amount
    remaining_amount = target_amount
    available_products = products.copy()
    
    while remaining_amount > 0 and available_products:
        # Select a random product
        product = random.choice(available_products)
        
        # Calculate maximum quantity we can afford
        max_quantity = min(4, int(remaining_amount / product['price']))
        
        if max_quantity == 0:
            # Can't afford this product, remove it from available products
            available_products.remove(product)
            continue
        
        # Random quantity between 1 and max_quantity
        quantity = random.randint(1, max_quantity)
        product_total = product['price'] * quantity
        
        # Remove last 2 characters (underscore and number) from product name
        clean_product_name = product['name'][:-2] if len(product['name']) > 2 else product['name']
        
        bill_products.append({
            'product_name': clean_product_name,
            'quantity': quantity,
            'unit_price': product['price'],
            'total_price': product_total
        })
        
        remaining_amount -= product_total
    
    # Calculate final total
    final_total = sum(p['total_price'] for p in bill_products)
    
    return {
        'bill_id': bill_id,
        'products': bill_products,
        'total_amount': round(final_total, 2)
    }

def generate_random_dates(start_date, end_date, num_dates):
    """Generate random dates between start and end date"""
    # Convert dates to Unix timestamps (floats)
    start_ts = start_date.timestamp()
    end_ts = end_date.timestamp()
    
    # Generate random timestamps between the range
    random_timestamps = np.random.uniform(start_ts, end_ts, num_dates)
    
    # Sort them to ensure they are in increasing order
    random_timestamps.sort()
    
    # Convert back to datetime objects
    random_datetimes = [datetime.fromtimestamp(ts) for ts in random_timestamps]
    
    # Strip time part and keep only dates
    random_dates = [dt.date() for dt in random_datetimes]
    
    # Create serial number to date mapping
    date_mapping = {}
    for i, date in enumerate(random_dates, 1):
        date_mapping[i] = date.strftime("%Y-%m-%d")
    
    return date_mapping

def generate_bills_with_start_id(number_of_bills, total_bill_amount, products_csv, start_bill_id=1):
    """Generate multiple bills with variety while matching target amount, starting from specific bill ID"""
    products = load_products(products_csv)
    
    if not products:
        print("No products loaded. Cannot generate bills.")
        return []
    
    bills = []
    target_per_bill = total_bill_amount / number_of_bills
    
    # Generate bills with variety around the target
    for i in range(number_of_bills):
        current_bill_id = start_bill_id + i
        # Create variation: ±40% around target, but clamp between $50 and $1500
        variation_factor = random.uniform(0.6, 1.4)  # ±40% variation
        bill_target = target_per_bill * variation_factor
        bill_target = max(50, min(1500, bill_target))  # Clamp between $50-$1500
        
        bill = generate_single_bill(current_bill_id, products, bill_target)
        bills.append(bill)
        print(f"Generated Bill {current_bill_id}: ${bill['total_amount']}")
    
    # Check totals and adjust if needed
    total_generated = sum(bill['total_amount'] for bill in bills)
    tolerance_percent = ((total_generated - total_bill_amount) / total_bill_amount) * 100
    
    print(f"\nTarget amount: ${total_bill_amount:.2f}")
    print(f"Generated amount: ${total_generated:.2f}")
    print(f"Difference: ${total_generated - total_bill_amount:.2f}")
    print(f"Tolerance: {tolerance_percent:.2f}%")
    
    if abs(tolerance_percent) <= 5:
        print("Within ±5% tolerance - EXCELLENT")
    elif abs(tolerance_percent) <= 10:
        print("Within ±10% tolerance - GOOD")
    elif abs(tolerance_percent) <= 20:
        print("Within ±20% tolerance - ACCEPTABLE")
    else:
        print("Outside ±20% tolerance - You may want to regenerate")
    
    return bills

def export_bills_to_csv(bills, output_filename="generated_bills.csv", date_mapping=None):
    """Export bills to CSV file"""
    with open(output_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Bill_ID', 'Date', 'Product_Name', 'Quantity', 'Unit_Price', 'Total_Price', 'Bill_Total'])
        
        # Write bill data
        for bill in bills:
            bill_date = date_mapping.get(bill['bill_id'], '') if date_mapping else ''
            for product in bill['products']:
                writer.writerow([
                    bill['bill_id'],
                    bill_date,
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

def append_bills_to_csv(bills, output_filename="generated_bills.csv", date_mapping=None):
    """Append bills to existing CSV file"""
    with open(output_filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write bill data (no header for append)
        for bill in bills:
            bill_date = date_mapping.get(bill['bill_id'], '') if date_mapping else ''
            for product in bill['products']:
                writer.writerow([
                    bill['bill_id'],
                    bill_date,
                    product['product_name'],
                    product['quantity'],
                    product['unit_price'],
                    product['total_price'],
                    bill['total_amount']
                ])
    
    print(f"\nBills appended to '{output_filename}'")
    print(f"Additional bills generated: {len(bills)}")
    total_generated = sum(bill['total_amount'] for bill in bills)
    print(f"Additional amount generated: ${total_generated:.2f}")

def main():
    """Main function to run the bill generator"""
    try:
        # Get user inputs
        start_date, end_date, fancy_bills, fancy_amount, cloths_bills, cloths_amount = get_user_inputs()
        
        if fancy_bills <= 0 or fancy_amount <= 0 or cloths_bills <= 0 or cloths_amount <= 0:
            print("Number of bills and total bill amounts must be positive.")
            return
        
        if start_date > end_date:
            print("Start date must be before end date.")
            return
        
        total_bills = fancy_bills + cloths_bills
        
        # Generate random dates for all bills
        print(f"\n=== Generating Random Dates ===")
        print(f"Generating {total_bills} random dates between {start_date.strftime('%Y-%m-%d')} and {end_date.strftime('%Y-%m-%d')}...")
        date_mapping = generate_random_dates(start_date, end_date, total_bills)
        print(f"Date mapping created for bills 1-{total_bills}")
        
        all_bills = []
        
        # Get script directory for absolute paths
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fancy_csv_path = os.path.join(script_dir, "products_fancy_items.csv")
        cloths_csv_path = os.path.join(script_dir, "products_cloths.csv")
        output_csv_path = os.path.join(script_dir, "generated_bills.csv")
        
        # Generate fancy items bills first
        print(f"\n=== Generating Fancy Items Bills ===")
        print(f"Generating {fancy_bills} bills...")
        fancy_bills_list = generate_bills_with_start_id(fancy_bills, fancy_amount, fancy_csv_path, 1)
        
        if fancy_bills_list:
            # Export fancy bills to CSV (this creates the file)
            export_bills_to_csv(fancy_bills_list, output_csv_path, date_mapping)
            all_bills.extend(fancy_bills_list)
            
            # Show sample of first fancy bill with date
            first_bill_id = fancy_bills_list[0]['bill_id']
            first_bill_date = date_mapping.get(first_bill_id, 'N/A')
            print(f"\n=== Sample Fancy Bill (Bill ID: {first_bill_id}, Date: {first_bill_date}) ===")
            print(f"Products:")
            for product in fancy_bills_list[0]['products']:
                print(f"  - {product['product_name']}: {product['quantity']} x ${product['unit_price']} = ${product['total_price']}")
            print(f"Total: ${fancy_bills_list[0]['total_amount']}")
        
        # Generate cloths bills with continuous numbering
        print(f"\n=== Generating Cloths Bills ===")
        print(f"Generating {cloths_bills} bills...")
        start_cloth_bill_id = fancy_bills + 1
        cloths_bills_list = generate_bills_with_start_id(cloths_bills, cloths_amount, cloths_csv_path, start_cloth_bill_id)
        
        if cloths_bills_list:
            # Append cloths bills to existing CSV
            append_bills_to_csv(cloths_bills_list, output_csv_path, date_mapping)
            all_bills.extend(cloths_bills_list)
            
            # Show sample of first cloth bill with date
            first_cloth_bill_id = cloths_bills_list[0]['bill_id']
            first_cloth_date = date_mapping.get(first_cloth_bill_id, 'N/A')
            print(f"\n=== Sample Cloth Bill (Bill ID: {first_cloth_bill_id}, Date: {first_cloth_date}) ===")
            print(f"Products:")
            for product in cloths_bills_list[0]['products']:
                print(f"  - {product['product_name']}: {product['quantity']} x ${product['unit_price']} = ${product['total_price']}")
            print(f"Total: ${cloths_bills_list[0]['total_amount']}")
        
        # Show final summary
        if all_bills:
            total_bills_count = len(all_bills)
            total_amount = sum(bill['total_amount'] for bill in all_bills)
            target_total = fancy_amount + cloths_amount
            tolerance_percent = ((total_amount - target_total) / target_total) * 100
            
            print(f"\n=== FINAL SUMMARY ===")
            print(f"Total bills generated: {total_bills_count}")
            print(f"Fancy bills: {fancy_bills}, Cloth bills: {cloths_bills}")
            print(f"Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
            print(f"Total target amount: ${target_total:.2f}")
            print(f"Total generated amount: ${total_amount:.2f}")
            print(f"Total difference: ${total_amount - target_total:.2f}")
            print(f"Total tolerance: {tolerance_percent:.2f}%")
            
            if abs(tolerance_percent) <= 5:
                print("Overall tolerance: EXCELLENT (±5%)")
            elif abs(tolerance_percent) <= 10:
                print("Overall tolerance: GOOD (±10%)")
            elif abs(tolerance_percent) <= 20:
                print("Overall tolerance: ACCEPTABLE (±20%)")
            else:
                print("Overall tolerance: Outside acceptable range")
        
    except ValueError as e:
        print(f"Error: Invalid input format. {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()