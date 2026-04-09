import csv
import random
import os
from collections import defaultdict

def modify_generated_csv(csv_file_path):
    """Modify the generated CSV by removing Bill_Total, shuffling rows, and recalculating totals"""
    
    # Check if file exists
    if not os.path.exists(csv_file_path):
        print(f"Error: File '{csv_file_path}' not found.")
        return False
    
    print(f"Reading CSV file: {csv_file_path}")
    
    # Read the original CSV
    rows = []
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    print(f"Original CSV has {len(rows)} rows")
    print(f"Original columns: {fieldnames}")
    
    # Step 1: Remove Bill_Total column
    print("\n=== Step 1: Removing Bill_Total column ===")
    if 'Bill_Total' in fieldnames:
        fieldnames.remove('Bill_Total')
        print("Bill_Total column removed")
    else:
        print("Bill_Total column not found")
    
    # Remove Bill_Total from each row
    for row in rows:
        if 'Bill_Total' in row:
            del row['Bill_Total']
    
    # Step 2: Extract product data and keep Bill_ID, Date, and Name intact
    print("\n=== Step 2: Extracting product data for global shuffling ===")
    
    # Separate static columns (Bill_ID, Date, Name) from shufflable columns (Product_Name, Quantity, Unit_Price, Total_Price)
    static_columns = []
    product_columns = []
    
    for row in rows:
        static_data = {
            'Bill_ID': row['Bill_ID'],
            'Date': row['Date'],
            'Name': row.get('Name', '')  # Handle case where Name might not exist
        }
        product_data = {
            'Product_Name': row['Product_Name'],
            'Quantity': row['Quantity'],
            'Unit_Price': row['Unit_Price'],
            'Total_Price': row['Total_Price']
        }
        static_columns.append(static_data)
        product_columns.append(product_data)
    
    print(f"Extracted {len(static_columns)} rows with static columns and product data")
    
    # Step 3: Shuffle product data globally
    print("\n=== Step 3: Shuffling product data globally ===")
    random.shuffle(product_columns)
    print(f"Shuffled {len(product_columns)} product entries globally")
    
    # Step 4: Recombine static columns with shuffled product data
    print("\n=== Step 4: Recombining static columns with shuffled products ===")
    shuffled_rows = []
    for i in range(len(static_columns)):
        combined_row = {
            'Bill_ID': static_columns[i]['Bill_ID'],
            'Date': static_columns[i]['Date'],
            'Name': static_columns[i]['Name'],
            'Product_Name': product_columns[i]['Product_Name'],
            'Quantity': product_columns[i]['Quantity'],
            'Unit_Price': product_columns[i]['Unit_Price'],
            'Total_Price': product_columns[i]['Total_Price']
        }
        shuffled_rows.append(combined_row)
    
    print(f"Created {len(shuffled_rows)} rows with globally shuffled products")
    
    # Step 5: Calculate Bill_Total for each bill
    print("\n=== Step 5: Calculating Bill_Total for each bill ===")
    bill_totals = {}
    
    # Group by Bill_ID to calculate totals
    bill_groups = defaultdict(list)
    for row in shuffled_rows:
        bill_id = row['Bill_ID']
        bill_groups[bill_id].append(row)
    
    for bill_id, group in bill_groups.items():
        total = 0.0
        for row in group:
            total += float(row['Total_Price'])
        bill_totals[bill_id] = round(total, 2)
        print(f"  Bill {bill_id}: ${bill_totals[bill_id]} (from {len(group)} products)")
    
    # Step 6: Add Bill_Total column back
    print("\n=== Step 6: Adding Bill_Total column back ===")
    fieldnames.append('Bill_Total')
    
    for row in shuffled_rows:
        bill_id = row['Bill_ID']
        row['Bill_Total'] = bill_totals[bill_id]
    
    # Step 7: Write the modified CSV
    print("\n=== Step 7: Writing modified CSV ===")
    
    # Create new output file instead of overwriting original
    output_file = csv_file_path.replace('.csv', '_globally_shuffled.csv')
    
    # Write modified CSV to new file
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(shuffled_rows)
    
    print(f"Modified CSV written to: {output_file}")
    print(f"Original file remains unchanged: {csv_file_path}")
    
    # Show sample of modified data
    print("\n=== Sample of Modified Data ===")
    print("First 10 rows of modified CSV:")
    for i, row in enumerate(shuffled_rows[:10]):
        print(f"  Row {i+1}: Bill_ID={row['Bill_ID']}, Date={row['Date']}, Name={row['Name']}, "
              f"Product={row['Product_Name'][:20]}..., Total=${row['Bill_Total']}")
    
    return True

def main():
    """Main function to run the CSV modifier"""
    try:
        # Get the CSV file path (same directory as this script)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(script_dir, "generated_bills.csv")
        
        print("=== CSV Modifier Tool ===")
        print(f"Target file: {csv_file_path}")
        
        # Check if user wants to proceed
        proceed = input(f"Do you want to modify '{csv_file_path}'? (y/n): ").lower()
        if proceed != 'y':
            print("Operation cancelled.")
            return
        
        # Modify the CSV
        success = modify_generated_csv(csv_file_path)
        
        if success:
            print("\n=== Operation Completed Successfully ===")
            print("The CSV file has been modified:")
            print("1. Bill_Total column removed")
            print("2. Rows shuffled (Bill_ID, Date, and Name kept together)")
            print("3. Bill_Total column recalculated and added back")
            print("4. Original file backed up")
        else:
            print("\n=== Operation Failed ===")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
