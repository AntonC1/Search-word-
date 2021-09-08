import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

print('Wpisz szukana statystyke :')
x = input()
trends = TrendReq()
keyword = trends.suggestions(keyword=x)
data = pd.DataFrame(keyword)
print(data.head())
