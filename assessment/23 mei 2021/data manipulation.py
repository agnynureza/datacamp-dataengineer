#1. menampilkan dataframe 
import pandas as pd 
print(df[['aligment', 'character']]) 

#2. method to see peek at the top of df ? head()

# 3. merubah data 
df.stars.transform(lambda x : x/1000) 

# 4. merubah semua df menjadi diakar
import numpy as np
df.apply(np.sqrt)

# 5. mencaari inter-quantile
q1 = df['age'].quantile(0.25)
q3 = df['age'].quantile(0.75)

print(q3 - q1)

# 6. bentuk grafik titik titik
import seaborn as sns 
import matplotlib.pyplot as plt
sns.scatterplot(data=steam,
                x="temp",
                y="usage") 
plt.show()

# 7.filter data di df
cond1 = food['protein'] < 10
cond2 = food['protein'] > 4 

food_subset = food[cond1 & cond2]
print(food_subset.sort_values('energy'))

# 8. mencari value di df 3 value terendah 
print(df.nsmallest(3, 'population'))

# 9. menghitung inter-quantile
from scipy import stats
iqr_age = stats.iqr(age)

# 10. membuat grafik bar horizontal
sns.barplot(x="val", y="lab", data=df)

# 11. buatgrafik 2x2 dimana col = time, row = smoker
g = sns.FacetGrid(
            tips,  
            col="time", 
            row="smoker"
            )

# 12. membuat grafik garis yang judul axisnya miring 45 derajat
sns.lineplot(
  x='date', 
  y='close', 
  data=amazon)

plt.xticks(rotation = 45)
plt.show()

# 13. mencari largest dari dataframe
largest = food[food['energy'] == food['energy'].max()]

# 14. buat grafik garis 
sns.lineplot(data= happiness, x='Overall rank', y='Score')

# 15. menghitung inter-quartile dengan numpy
IQR = stats.iqr(pH)
print(IQR)