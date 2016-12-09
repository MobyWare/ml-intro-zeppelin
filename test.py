import numpy as np
import pandas as pd
df = pd.read_csv('notebooks/home_data.csv')
data = df[[0,4,5]][0:2].as_matrix()
#data = np.array([['1','2','3'],['4','5','6']])
print(data)
rowOut = None
output = None

for row in data:
	rowOut = None
	for col in row:		
		if rowOut is None:
			rowOut = str(col)
		else:
			rowOut = rowOut + '\t' + str(col)
	if output is None:
		output = rowOut
	else:
		output = output + '\n' + rowOut

print(output)
