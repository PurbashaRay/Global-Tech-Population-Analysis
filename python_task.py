import pandas as pd
import matplotlib.pyplot as plt
file_path ="RR-PRAC3 - population.csv" #file path
df=pd.read_csv(file_path) #load the csv file

###################################################  QUESTION 1  ############################################################
# Question 1.How many countries had no recorded population data (0) for the year 2000? List these countries along with their regions

'''#filtered country with 0 population in year 2000 
zero_population = df[(df['year'] == 2000) & (df['population'] == 0 )] 

#selected columns 'country name' and 'continent'
zero_pop_country = zero_population[['country name','continent']]


#displayed number of countries with zero population.Used nunique() on zero_pop_country variable to get the number of unique values.
num_country=zero_pop_country['country name'].nunique()

#output
print(f"\n\nNumber of countries with zero population in 2000:\n {num_country}")
print(f"\n\nList of countries who have zero population is year 2000: \n{zero_pop_country}")'''



###########################################  QUESTION 2  ##############################################################################
#Calculate the total population for all African countries in 2010.Create a bar chart showing the population distribution across African countries in 2010.

'''#filetered the countries in continent 'Africa' of year 2010
africa_pop_2010= df[(df['continent'] == 'Africa') & (df['year'] == 2010 )]

#sum of the population of all african countries in year 2010 and the print statement
total_pop_africa =int(africa_pop_2010['population'].sum())
print(f"The total population for all african countries in 2010 :\n{total_pop_africa} Million")

# bar chart of population distribution of african countires in year 2010

plt.figure(figsize=(12,6),facecolor='lightyellow')  
plt.bar(africa_pop_2010['country name'],africa_pop_2010['population'],color='green')
plt.xticks(rotation=90) 
plt.title('Population Distribution Across African Countries in 2010',weight='bold') 
plt.grid(axis='y', linestyle='--', alpha=0.5) 
plt.xlabel('African Countries',fontweight='bold')  
plt.ylabel('Population',fontweight='bold')  
plt.tight_layout()  
plt.show()'''

###################################################  QUESTION 3  ####################################################

#Determine the average population of countries in South America for the year 2000.Highlight countries with populations above and below this average. Include the lists in your analysis.

'''SA_country_2000=df[(df['continent'] == 'South America') & (df['year'] == 2000)]
avg_pop= SA_country_2000['population'].mean()
print(f"**The average population of countries in South America for the year 2000** \n {avg_pop}")

coun_below_avg=SA_country_2000[SA_country_2000['population'] < avg_pop]
print(f"**Countries population below average**\n{coun_below_avg[['country name','population']]}")
coun_above_avg=SA_country_2000[SA_country_2000['population'] >= avg_pop]
print(f"\n\n**Countries population above average**\n{coun_above_avg[['country name','population']]}")

#Bar chart with analysis
plt.figure(figsize=(11,6))
plt.bar(SA_country_2000['country name'],SA_country_2000['population'],color=['green' if pop >= avg_pop else 'red' for pop in SA_country_2000['population']])
plt.xticks(rotation=90)
plt.axhline(avg_pop, color='blue', linestyle='--')
plt.title("Countries with populations above and below average(24.5)", weight='bold')
plt.xlabel("Countries", weight='bold')
plt.ylabel("Population", weight='bold')
plt.tight_layout()
plt.show()'''

############################################  QUESTION 4    #######################################################################
#Identify the countries with populations exceeding 1000 million in 2007.Create a bar chart or scatter plot to display all countries' populations in 2007, marking those above 1000.

'''# Filter for the year 2007
country_2007 = df[df['year'] == 2007]

# Sort countries by population (largest to smallest)
country_2007 = country_2007.sort_values(by='population', ascending=False)

# Find countries with population > 1000 million
big_countries = country_2007[country_2007['population'] > 1000]
print("Countries with population > 1000 million in 2007:\n")
print(big_countries[['country name', 'continent', 'population']])

# Colors: red for >1B, blue for others
colors = ['red' if p > 1000 else 'skyblue' for p in country_2007['population']]

# Scatter plot 1: All countries 
plt.figure(figsize=(14, 6))
plt.scatter(country_2007['country name'], country_2007['population'], color=colors,edgecolors='black')
plt.xticks(rotation=45, fontsize=6)
plt.title("Population of All Countries (2007)")
plt.xlabel("Country")
plt.ylabel("Population (millions)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Scatter plot 2: Top 20 countries 
top20 = country_2007.head(20)
colors_top20 = ['red' if p > 1000 else 'green' for p in top20['population']]

plt.figure(figsize=(10, 6))
plt.scatter(top20['country name'], top20['population'], color=colors_top20,s=80,edgecolors='black')
plt.xticks(rotation=45, ha='right')
plt.title("Top 20 Most Populous Countries (2007)")
plt.ylabel("Population (millions)")
plt.xlabel("Country")
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()'''


#####################################   QUESTION 5  ################################################
#Calculate the total population growth in Europe between 2000 and 2010.Identify the top 5 European countries by population growth during this period
#and create a line plot showing the population changes of these countries from 2000 to 2010

'''# Filter for Europe and the years 2000 & 2010
europe_country= df[(df ["continent"] == 'Europe')&(df['year'].isin([2000,2010]))]

#Calculate total European population in 2000 and 2010
sum_2000 = europe_country[europe_country['year'] == 2000]['population'].sum()
sum_2010 = europe_country[europe_country['year'] == 2010]['population'].sum()

#total population growth
total_growth= sum_2010-sum_2000
print(f"Total growth in Europe between 2000 and 2010:\n{total_growth} Million")

#Calculate population growth per country
growth = (
    europe_country.pivot_table(
        index='country name',
        columns='year',
        values='population'
    ).reset_index()
   )
growth['growth'] = growth[2010]-growth[2000]
growth['growth rate'] =((growth[2010]-growth[2000])/growth[2000])*100

# Top 5 countries by growth
top_5= growth.sort_values(by='growth',ascending=False).head(5)
print(f"The top 5 European countries with highest growth rate :")
print(top_5[['country name', 'growth','growth rate']])

# Filter only those 5 countries from the full dataset
final_data = df[
    (df['continent'] == 'Europe') &
    (df['country name'].isin(top_5['country name'])) &
    (df['year'].between(2000, 2010))
]

#Line plot for Analysis
plt.figure(figsize=(10, 6))
for country in top_5['country name']:
    sub_data = final_data[final_data['country name'] == country]
    plt.plot(sub_data['year'], sub_data['population'], marker='o', label=country)

plt.title('Population Change between 2000–2010(Top 5 European Countries by Growth) ')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()'''


