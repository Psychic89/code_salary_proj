# Data Science City Estimator: Project overview
* Objective is to identify the ideal city in Germany for a data scientist to looking for a job
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

# Project walk-through
* Ken Jee: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

# Webscraping overview
* Modified the above webscraper to scrape over 350 data science job posts in Germany

# Scraped data
* Job-Titel
* Stellenbeschreibung
* Bewertung
* Firmenname
* Ort
* Hauptsitz
* Firmengröße
* Gegründet
* Rechtsform
* Branche
* Industriezweig
* Umsatz
* Konkurrenten
