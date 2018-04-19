import pandas as pd
from collections import OrderedDict
from datetime import date

sales = OrderedDict([ ('account', ['Jones LLC', 'Alpha Co', 'Blue Inc']),
          ('Jan', [150, 200, 50]),
          ('Feb',  [200, 210, 90]),
          ('Mar', [140, 215, 95]) ] )
df = pd.DataFrame.from_dict(sales)

print(df.sort_values('account'))

food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
print(food['ham'])
print (df.empty)