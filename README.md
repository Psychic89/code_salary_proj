# Data Science City Predictor: Project overview
* Objective is to identify the ideal city in Germany for a data scientist looking for a job
* Scraped glassdoor.com for over 350 data science job posts in germany
* Performed data cleaning and engineered features such as quantifying the value companies place on specific programming languages from the job description
* Created and optimized linear, random forest and Lasso regressors intil the best model was attained

# Next step
* Deploying the model using Flask

## Code and resources
* Python Version: 3.8.3
* Packages used: pandas, sklearn, mumpy, matplotlib, selenium, seaborn
* Scraper used: https://github.com/arapfaik/scraping-glassdoor-selenium
* Article on how to use the scraper: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

# Webscraping overview
* Modified the above webscraper to scrape over 350 data science job posts in Germany

# Scraped data
* Job-Titel (Job title)
* Stellenbeschreibung (Job Description)
* Bewertung (Rating)
* Firmenname (Company)
* Ort (Location)
* Hauptsitz (Company Headquarters)
* Firmengröße (Company Size)
* Gegründet (Company Founded Date)
* Rechtsform (Type of Ownership)
* Branche (Industry)
* Industriezweig (Sector)
* Umsatz (Revenue)
* Konkurrenten (Competitors)

# Cleaning the data
Now that we have scraped the data, it's time to clean it. We need to make sure that it is usable for our model, so we made a few changes and created new variables.
*   Parsed rating from the company tex
*   Created a new column for job city
*   Created a new column for job country
*   Added a column for if the company's headquarters was located in the same city as that of the company
*   Extracted company age from founded date
*   Created columns for each programming skill required from the job description
    * Python
    * R
    * Spark
    * aws
    * Excel
*   Created column for the simplified job title
*   Created column for the description length

# Exploratory Data Analysis (EDA)
I observed the data distribution and value counts for several categorical variables to gather some insights. These are some of the highlights. 

![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/companies.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/headquarters.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/job_at_hq.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/job_roles.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/leading_industries.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/most_ds_jobs.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/python.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/R.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/salaries.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/sql.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/type_of_company.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/avg%20_rating_for_job_role.png)
![alt text](https://github.com/Psychic89/code_salary_proj/blob/master/python_company_revenue.png)

# Building the model
All categorical variables were converted to dummy variables. I then split the data into two sets:
*   train set (80%)
*   test set (20%)

I experimented with multiple linear regression model, lasso regression model and random forest model and evaluated them using Mean Absolute Error (MAE). MAE is relatively easier to interpret and we can get away with a few outliers in our data.

# How the models performed
I converted all categorical variables to dummy variables. I then split the data into two sets:
*   Random Forest: MAE = 11,14
*   Linear Regression: MAE = 18.96
*   Lasso Regression: MAE = 20.06

Random Forest model emerged to be the best performing model on the test and validation sets.

# NEXT STEP: Deploying the model into production
The next step will be to create a Flask API endpoint on a locally hosted webserver. The API endpoint will be able to receive a request from a job listing and returning the best city.
