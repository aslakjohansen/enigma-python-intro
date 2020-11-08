import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('dkbirths2019.csv', names=['day', 'raw'])
df['avgw'] = df['raw'].rolling(window=7, center=True).mean()
df['avgm'] = df['raw'].rolling(window=30, center=True).mean()

plt.figure(figsize=[15,10])
plt.xlabel('Time/[days]')
plt.ylabel('Births/[#]')
plt.plot(df['day'], df['raw'],label='reported value')
plt.plot(df['day'], df['avgw'],label='weekly running average')
plt.plot(df['day'], df['avgm'],label='monthly running average')
plt.legend(loc=2)
plt.savefig('running-average.pdf')
