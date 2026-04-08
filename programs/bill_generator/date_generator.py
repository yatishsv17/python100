import pandas as pd
import numpy as np
from datetime import datetime

def get_user_inputs():
    """Get user inputs for date generation"""
    print("=== Random Date Generator ===")
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    num_dates = int(input("Enter number of dates to generate: "))
    
    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    
    return start_date, end_date, num_dates

# 1. Get user inputs
start_date, end_date, num_dates = get_user_inputs()

# 2. Convert dates to Unix timestamps (floats)
start_ts = start_date.timestamp()
end_ts = end_date.timestamp()

# 3. Generate random timestamps between the range
# Using numpy.random.uniform for a continuous distribution
random_timestamps = np.random.uniform(start_ts, end_ts, num_dates)

# 4. Sort them to ensure they are in increasing order
random_timestamps.sort()

# 5. Convert back to datetime objects
random_datetimes = [datetime.fromtimestamp(ts) for ts in random_timestamps]

# 6. Strip time part and keep only dates
random_dates = [dt.date() for dt in random_datetimes]

# 7. Create serial numbers (1 to num_dates)
serial_numbers = list(range(1, num_dates + 1))

# 8. Write to CSV using pandas with both serial number and date columns
df = pd.DataFrame({
    'serial_number': serial_numbers,
    'date': random_dates
})
df.to_csv('random_datetimes.csv', index=False)

print(f"Successfully generated {num_dates} random dates with serial numbers in 'random_datetimes.csv'")
