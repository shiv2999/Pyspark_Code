# Python code demonstrate creating 
# DataFrame from dict narray / lists 
# By default addresses.
 
import pandas as pd
 
# intialise data of lists.
data = {'Name':['Tom', 'nick', 'krish', 'jack', 'Govind'],
        'Age':[20, 21, 19, 18, '21']}
 
# Create DataFrame
df = pd.DataFrame(data)
 
# Print the output.
print(df)

# Display the output.
display(df)
