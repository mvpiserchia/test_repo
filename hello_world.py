import pandas as pd

print('Hello, World!')
print('Upload to Git was a success!')

df = pd.DataFrame({'Age': [34,56,18], 'Name': ['Jen', 'Mark', 'Dan']})
print(df)

verbose_var_list = ['One variable in df is named ' + i for i in df.columns]
print(verbose_var_list)
