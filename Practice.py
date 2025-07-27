import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('movie_ratings.csv')

print(df['Rating'].mean())

print(df.sort_values(by='Rating', ascending=False).head(10))
below30 =df[df['Rating'] >= 8]

movie_ratings = df.groupby('Genre')['Rating'].mean()

plt.figure(figsize = (10,10))

movie_ratings.plot(kind = 'bar',color = 'blue')
plt.title('Genre Ratings')
plt.xlabel('Genre Title')
plt.ylabel('Genre Rating')
plt.show()

print(below30)