##   GLOBAL TECH COMPANY : Population Analysis Project

This project analyzes global population data using pandas and matplotlib.pyplot. 
The dataset is loaded from RR-PRAC3-population.csv into a DataFrame df. All analyses are performed using Python scripts, primarily in python_task.py.

####    Dataset: [Data](https://github.com/PurbashaRay/Global-Tech-Population-Analysis/blob/4dab4f195cd5f248f91398db2002fb6826cab3af/RR-PRAC3%20-%20population.csv)
####    Fields: 
        ID
        Country name
        Continent
        Populataion (in Millions)
        Year


####  How to Run the Code:
- Open the file python_task.py,each question’s solution is written in a separate code block within the file.
- Remove the triple quotes (''') used to comment out the section.
- Run the code to view the output and visualizations.
- Repeat the same process for other questions to explore their results and charts.


###  Q1: How many countries had no recorded population data (0) for the year 2000? List these countries along with their regions.

##### Result:
There are a total of 59 countries with a recorded population of zero in the year 2000.
The list of these countries, along with their respective regions, can be viewed by running the code for Question 1.

##### Analysis:
I filtered the countries with a recorded population of 0 in the year 2000 using an & condition on the population and year columns from df, and stored the result in zero_population.
Then, I selected the country name and continent columns from this data and assigned it to zero_pop_country.
Using the nunique() function on the country name column of zero_population, I obtained the number of unique countries and stored it in the variable num_country.
Finally, I printed num_country to display the number of unique countries with a population of 0, along with the list of those countries.

##### Insight:
Missing data or incomplete reporting.Population cannot be recorded as 0.

### Q2: Calculate the total population for all African countries in 2010. Create a bar chart showing the population distribution across African countries in 2010.

##### Result:
The total population of all African countries in 2010 is 991 Million.

##### Analysis:
I filtered the dataset for African countries in the year 2010 and stored it in the variable africa_pop_2010.
Using the .sum() function, I calculated the total population and assigned it to total_sum_africa.
To visualise the population distribution across all African countries in 2010, I created a bar chart with country names on the x-axis and population on the y-axis.

Chart: ![African population chart 2010](https://github.com/PurbashaRay/Global-Tech-Population-Analysis/blob/4dab4f195cd5f248f91398db2002fb6826cab3af/Question2.png)

##### Insight:
Among African countries in 2010, Nigeria and Ethiopia had the highest populations, while approximately 9 countries reported a population of 0, indicating missing or unrecorded data.

###  Q3: Determine the average population of countries in South America for the year 2000. Highlight countries with populations above and below this average. Include the lists in your analysis.

##### Result:
The average population of countries in South America is 24.5 Millions.
The countries above average are :Argentina, Brazil, Colombia, Peru
The countries below average are : Bolivia, Chile, Ecudor,Falkland Islands,French Guiane,Guyana,Paraguay,Suriname,Uruguay,Venezuela

##### Analysis:
I filtered the dataset for countries in South America in the year 2000 and stored the result in SA_country_2000.
I calculated the average population using .mean() and stored it in avg_pop.
Countries with population above the average were stored in coun_above_avg, and the remaining countries were stored in coun_below_avg. Both lists were displayed for reference.
Finally, I created a bar chart to visualize the population of all South American countries, highlighting which countries are above or below the average.

 Chart:![SA population in 2000](https://github.com/PurbashaRay/Global-Tech-Population-Analysis/blob/4dab4f195cd5f248f91398db2002fb6826cab3af/Question3.png)

Insight:
This highlights population concentration in a few major nations versus sparsely populated regions.

###  Q4: Identify the countries with populations exceeding 1000 million in 2007. Create a bar chart or scatter plot to display all countries' populations in 2007, marking those above 1000.

##### Result:
China and India had populations exceeding 1 billion in 2007.

##### Analysis:
I filtered the dataset for all countries in the year 2007 and stored it in country_2007.
The data was sorted by population, and countries with a population exceeding 1000 million were stored in big_countries. The list of these countries was displayed for reference.
Since there are 213 countries in the dataset for the year 2007, the chart displaying all countries appeared cluttered and difficult to read.To improve clarity, I created two charts: one showing the population of all countries in 2007, and another focusing on the top 20 most populous countries.
The x-axis represents country names, and the y-axis represents population.
Countries with populations exceeding 1000 million are highlighted in red, while the rest are shown in green for clear visual distinction.

Chart1 ![All countries in year 2007](https://github.com/PurbashaRay/Global-Tech-Population-Analysis/blob/4dab4f195cd5f248f91398db2002fb6826cab3af/Question4_1.png)
Chart2 ![Top 20 Country](https://github.com/PurbashaRay/Global-Tech-Population-Analysis/blob/4dab4f195cd5f248f91398db2002fb6826cab3af/Question4_2.png)

##### Insight:
Population distribution shows a long tail, with most countries below 200 million, emphasizing global population imbalance.

###  Q5: Calculate the total population growth in Europe between 2000 and 2010. Identify the top 5 European countries by population growth during this period, and create a line plot showing the population changes of these countries from 2000 to 2010.

##### Result:
The total growth in Europe between 2000 and 2010 is -8 Million
The top 5 european countries with hightest growth rate(in descending order): 
Spain
France
United Kingdom
Ireland
Italy

##### Analysis:
I filtered the dataset for countries in Europe for the years 2000 to 2010 and stored it in europe_country.
To calculate the total population growth, I found the difference between the total population in 2010 and 2000, and stored the result in total_growth and displayed it .
I then created a pivot table named growth, which transformed the data from europe_country dataset into a table where each row represents a country, each column represents a year, and the corresponding population values fill the table.
Using this pivot table, I calculated both the absolute growth and growth rate for each country.
Finally, I created a line chart to visualize the population growth trends of the top 5 European countries during this period.

Chart:![Top5 European country](https://github.com/PurbashaRay/Global-Tech-Population-Analysis/blob/4dab4f195cd5f248f91398db2002fb6826cab3af/question5.png)


##### Insights:
Spain recorded the highest population growth rate in Europe during the period 2000–2010.
Overall, the continent experienced a population decline of approximately 8 million, which may reflect low birth rates, an aging population, and various economic factors affecting demographic trends.


### CONCLUSION:
This analysis highlights how population dynamics vary significantly across regions and time periods.
The data also reveals disparities in data reporting, with several countries showing zero population records, likely due to missing or incomplete data.
Overall, the project demonstrates how data analytics and visualization can uncover meaningful global patterns from identifying outliers and growth leaders to understanding regional demographic challenges.
These insights can serve as a foundation for further analysis of population trends, economic development, and resource planning across the world.

