import pandas as pd
import matplotlib.pyplot as plt

# Path to your file
path = r"C:\Users\rujut\OneDrive\RU_1 - Copy\ALL0000\F0000CH1.CSV"
path2 = r"C:\Users\rujut\OneDrive\RU_1 - Copy\ALL0000\F0000CH2.CSV"
# This CSV has metadata in cols 0–2, and the actual waveform in cols 3 (time) and 4 (voltage)
df = pd.read_csv(path, header=None, usecols=[3, 4], names=["time_s", "voltage_V"])

# Ensure numeric + drop any bad rows
df["time_s"] = pd.to_numeric(df["time_s"], errors="coerce")
df["voltage_V"] = pd.to_numeric(df["voltage_V"], errors="coerce")
df = df.dropna()

plt.figure()
plt.plot(df["time_s"], df["voltage_V"])
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("CH1 Waveform")
plt.grid(True)
plt.tight_layout()
plt.show()
