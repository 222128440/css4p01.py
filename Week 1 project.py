# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:38:15 2024

@author: ngoni
"""

import pandas as pd
import numpy as np

file = pd.read_csv("movie_dataset.csv")


# Allows you to see all rows
#pd.set_option('display._columns',None)

#print(file)

# x = [1,2,3,4,5,6]

# for i in x:
#     print(i)

file.columns = file.columns.str.replace(' ', '') 
print(file)


# file[['Revenue(Millions)','Metascore']] = \
#     file[['Revenue(Millions)','Metascore']].apply(lambda col: col.replace(np.nan, np.mean()))

x = file["Revenue(Millions)"].mean()

file["Revenue(Millions)"].fillna(x, inplace = True)

print(file)

y = file["Metascore"].mean()

file["Metascore"].fillna(y, inplace = True)

print(file)

z = file["Rating"].max()
print(file)

result_row = file[file['Rating'] == 9.0]

# Print the result
print("Row with Rating 9.0:")
print(result_row)

average = file["Revenue(Millions)"].mean()


print(average)

filtered_file = file[(file['Year'] >= 2015) & (file['Year'] <= 2017)]

# Calculate the average revenue
average_revenue = filtered_file['Revenue(Millions)'].mean()

# Print the result
print(filtered_file)
# print(info())

d = len(file[file['Year'] == 2016])

# Print the result
print(d)


t = file[file['Director'] == 'Christopher Nolan'].shape[0]

# Print the result
print(t)

# result_rows = file[file['Director'] == 'Christopher Nolan']]

# print("Rows with Director Chrostopher Nolan")

# print(result_rows)

high_rated_movies = file[file['Rating'] >= 8.0]

# Print the result
print("Movies with a rating of at least 8.0:")
print(high_rated_movies)


nolan_movies = file[file['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating = nolan_movies['Rating'].median()

# Print the result
print(f"The median rating of movies directed by Christopher Nolan is: {median_rating}")


average_rating_by_year = file.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
year_highest_average_rating = average_rating_by_year.idxmax()
highest_average_rating = average_rating_by_year.max()

# Print the result
print(f"The year with the highest average rating is {year_highest_average_rating} with an average rating of {highest_average_rating:.2f}")

movies_2006 = file[file['Year'] == 2006].shape[0]
movies_2016 = file[file['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

# Print the result
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {percentage_increase:.2f}%")

bradley_cooper_movies = file[file['Actors'].str.contains('Bradley Cooper')]

# Print the result
print("Movies with Bradley Cooper as an actor:")
print(bradley_cooper_movies[['Title', 'Actors']])


bradley_cooper_movies = file[file['Actors'].str.contains('Matthew McConaughey')]

# Print the result
print("Movies with Bradley Cooper as an actor:")
print(bradley_cooper_movies[['Title', 'Actors']])


unique_genres_count = file['Genre'].nunique()

# Print the result
print(f"The number of unique genres in the dataset is: {unique_genres_count}")


total_genres_count = file['Genre'].count()

# Print the result
print(f"The total number of genres in the dataset is: {total_genres_count}")


# correlation_matrix = file.corr().

#  # Print the correlation matrix
# print("Correlation Matrix:")
# print(correlation_matrix)


correlation = file['Runtime(Minutes)'].corr(file['Rating'])

# Print the correlation coefficient
print(f"The correlation between movie runtime and rating is: {correlation:.2f}")



a = file['Revenue(Millions)'].corr(file['Rating'])


print(a)


Rating_votes = file['Votes'].corr(file['Rating'])


print(Rating_votes)



Revenue_votes = file['Votes'].corr(file['Revenue(Millions)'])


print(Revenue_votes)


Revenue_runtime = file['Runtime(Minutes)'].corr(file['Revenue(Millions)'])


print(Revenue_runtime)


Revenue_year = file['Year'].corr(file['Revenue(Millions)'])


print(Revenue_year)


Revenue_Metascore = file['Metascore'].corr(file['Revenue(Millions)'])


print(Revenue_Metascore)


Rating_Metascore = file['Metascore'].corr(file['Rating'])


print(Rating_Metascore)

Runtime_Votes = file['Runtime(Minutes)'].corr(file['Votes'])


print(Runtime_Votes)