import pandas as pd
import numpy as np
from datetime import datetime

# 1. Define your start and end dates
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 3, 31)

# 2. Convert dates to Unix timestamps (floats)
start_ts = start_date.timestamp()
end_ts = end_date.timestamp()

# 3. Generate 100 random timestamps between the range
# Using numpy.random.uniform for a continuous distribution
random_timestamps = np.random.uniform(start_ts, end_ts, 185)

# 4. Sort them to ensure they are in increasing order
random_timestamps.sort()

# 5. Convert back to datetime objects
random_datetimes = [datetime.fromtimestamp(ts) for ts in random_timestamps]

# 6. Write to CSV using pandas
df = pd.DataFrame(random_datetimes, columns=['random_datetime'])
df.to_csv('random_datetimes.csv', index=False)

print("Successfully generated 185 random dates in 'random_datetimes.csv'")
