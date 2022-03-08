import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("rainfall_dataset.csv")

max_rainfall=df['ANNUAL'].max()
min_rainfall=df['ANNUAL'].min()
no_of_sub_div=df['ANNUAL'].count()
total_rainfall=df['ANNUAL'].sum()

val=df[df['ANNUAL']==max_rainfall]
for i in val['SUBDIVISION']:
    print(i)

val=df[df['ANNUAL']==min_rainfall]
for i in val['SUBDIVISION']:
    print(i)

# print("Min Rainfall of a month")
# month=input()
# min_month=df[month].min()
# val = df[df[month] == min_month]
# for i in val['SUBDIVISION']:
#     print(i)
#
# print("Min Rainfall of a month")
# month=input()
# min_month=df[month].min()
# val = df[df[month] == min_month]
# for i in val['SUBDIVISION']:
#     print(i)

groups=df.groupby(by='SUBDIVISION')
list_of_sub_div=list(groups.groups.keys())
list_of_annual_mean_rainfall=[]
for i in groups.groups.keys():
    data=groups.get_group(i)
    value=data['ANNUAL'].mean()
    list_of_annual_mean_rainfall.append(value)
plt.barh(list_of_sub_div,list_of_annual_mean_rainfall)
plt.show()

for i in groups.groups.keys():
    data=groups.get_group(i)
    value=data['ANNUAL'].mean()
    list_of_annual_mean_rainfall.append(value)
plt.plot(list_of_annual_mean_rainfall)
plt.show()