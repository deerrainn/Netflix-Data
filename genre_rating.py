#install libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#load the csv data into a data fram
data_path = 'netflix1.csv'
netflix_data = pd.read_csv(data_path)


#value counts per rating
rating = netflix_data["rating"].value_counts()
rating


popular_ratings = netflix_data.groupby('listed_in')['rating'].agg(lambda x: x.value_counts().idxmax())
#convert to data frame for plotting
popular_ratings_df = popular_ratings.reset_index()


#sort genres by number of occurences
popular_ratings_df['count'] = netflix_data.groupby('listed_in')['rating'].count()
top_genres = popular_ratings_df.sort_values(by='count', ascending=False).head(20)


#plot results in bar graph
#adjust figure size
plt.figure(figsize=(20, 10))
plt.bar(top_genres['listed_in'], top_genres['rating'], color='maroon')
plt.ylabel('Most Popular Rating', fontsize=16)
plt.xlabel('Genre', fontsize=17)
plt.title('Popular Rating per Genre', fontsize=20)
#rotate and align ticks
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
#use tight layout to avoid overlapping
plt.tight_layout()
# Show the plot
#plt.show()
#save plot
plt.savefig('rating_genre.png')
