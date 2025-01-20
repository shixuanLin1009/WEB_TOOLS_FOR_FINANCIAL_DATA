
import numpy as np
import talib

# Sample data for testing
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Calculate a 3-period simple moving average (SMA)
sma = talib.SMA(data, timeperiod=3)

print("Input Data:", data)
print("3-Period Simple Moving Average:", sma)