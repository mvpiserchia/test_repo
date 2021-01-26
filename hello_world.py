import pandas as pd

print('Hello, World!')
print('Upload to Git was a success!')

df = pd.DataFrame({'Age': [34,56,18], 'Name': ['Jen', 'Mark', 'Dan']})
print(df)

var_list = list(df.columns)
print('\n' + 'The first variable in df is {0}.'.format(var_list[0]))