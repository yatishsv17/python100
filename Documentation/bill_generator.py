import csv
import random

def get_user_inputs():
    """Get user inputs for bill generation"""
    print("=== Bill Generator ===")
    number_of_bills = int(input("Enter number of bills to generate: "))
    total_bill_amount = float(input("Enter total bill amount target: "))
    products_csv = input("Enter products CSV file path (default: products.csv): ") or "products.csv"
    
    return number_of_bills, total_bill_amount, products_csv

def load_products(products_csv):
    """Load products from CSV file"""
    products = []
    print(f"Loading products from: {products_csv}")
    try:
        with open(products_csv, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Handle both BOM and non-BOM column names
                product_name_key = None
                product_price_key = None
                
                for key in row.keys():
                    if key.replace('ï»¿', '') == 'Product_Name':
                        product_name_key = key
                    elif key.replace('ï»¿', '') == 'Product_Price':
                        product_price_key = key
                
                if not product_name_key or not product_price_key:
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
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Error: Products file '{products_csv}' not found.")
        return []
    except Exception as e:
        print(f"Error reading products file: {e}")
        return []
    
    print(f"Loaded {len(products)} products")
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
        max_quantity = min(5, int(remaining_amount / product['price']))
        
        if max_quantity == 0:
            # Can't afford this product, remove it from available products
            available_products.remove(product)
            continue
        
        # Random quantity between 1 and max_quantity
        quantity = random.randint(1, max_quantity)
        product_total = product['price'] * quantity
        
        bill_products.append({
            'product_name': product['name'],
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

def generate_bills(number_of_bills, total_bill_amount, products_csv):
    """Generate multiple bills that add up to target amount"""
    products = load_products(products_csv)
    
    if not products:
        print("No products loaded. Cannot generate bills.")
        return []
    
    bills = []
    target_per_bill = total_bill_amount / number_of_bills
    
    for i in range(1, number_of_bills + 1):
        bill = generate_single_bill(i, products, target_per_bill)
        bills.append(bill)
        print(f"Generated Bill {i}: ${bill['total_amount']}")
    
    # Check totals
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

def export_bills_to_csv(bills, output_filename="generated_bills.csv"):
    """Export bills to CSV file"""
    with open(output_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Bill_ID', 'Product_Name', 'Quantity', 'Unit_Price', 'Total_Price', 'Bill_Total'])
        
        # Write bill data
        for bill in bills:
            for product in bill['products']:
                writer.writerow([
                    bill['bill_id'],
                    product['product_name'],
                    product['quantity'],
                    product['unit_price'],
                    product['total_price'],
                    bill['total_amount']
                ])
    
    print(f"\nBills exported to '{output_filename}'")
    total_generated = sum(bill['total_amount'] for bill in bills)
    print(f"Total bills generated: {len(bills)}")
    print(f"Total amount generated: ${total_generated:.2f}")

def main():
    """Main function to run the bill generator"""
    try:
        # Get user inputs
        number_of_bills, total_bill_amount, products_csv = get_user_inputs()
        
        if number_of_bills <= 0 or total_bill_amount <= 0:
            print("Number of bills and total bill amount must be positive.")
            return
        
        # Generate bills
        print(f"\nGenerating {number_of_bills} bills...")
        bills = generate_bills(number_of_bills, total_bill_amount, products_csv)
        
        if bills:
            # Export to CSV
            export_bills_to_csv(bills)
            
            # Show sample of first bill
            print(f"\n=== Sample Bill (Bill ID: {bills[0]['bill_id']}) ===")
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
