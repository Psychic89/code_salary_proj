# -*- coding: utf-8 -*-





from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = "https://www.glassdoor.de/Job/Jobs.htm?sc.generalKeyword=%22data+scientist%22&sc.locationSeoString=deutschland&locId=96&locT=N"

    #url = "https://www.glassdoor.de/Job/Jobs.htm?sc.generalKeyword="+keyword+"
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
            driver.find_element_by_class_name("selected").click()
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
        except NoSuchElementException:
            pass

        
        #Going through each job in this page
        job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  #You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    firmenname = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                    ort = driver.find_element_by_xpath('.//div[@class="location"]').text
                    job_titel = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                    stellenbeschreibung = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    time.sleep(5)

            try:
                geschätztes_bruttogehalt = driver.find_element_by_xpath('.//span[@class="gray salary"]').text
            except NoSuchElementException:
                geschätztes_bruttogehalt = -1 #You need to set a "not found value. It's important."
            
            try:
                bewertung = driver.find_element_by_xpath('.//span[@class="rating"]').text
            except NoSuchElementException:
                bewertung = -1 #You need to set a "not found value. It's important."

            #Printing for debugging
            if verbose:
                print("Job-Titel: {}".format(job_titel))
                print("Geschätztes Bruttogehalt: {}".format(geschätztes_bruttogehalt))
                print("Stellenbeschreibung: {}".format(stellenbeschreibung[:500]))
                print("Bewertung: {}".format(bewertung))
                print("Firmenname: {}".format(firmenname))
                print("Ort: {}".format(ort))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()

                try:
                    #<div class="infoEntity">
                    #    <label>Hauptsitz</label>
                    #    <span class="value">Berlin (Deutschland)</span>
                    #</div>
                    hauptsitz = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Hauptsitz"]//following-sibling::*').text
                except NoSuchElementException:
                    hauptsitz = -1

                try:
                    firmengröße = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Größe"]//following-sibling::*').text
                except NoSuchElementException:
                    firmengröße = -1

                try:
                    gegründet = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Gegründet"]//following-sibling::*').text
                except NoSuchElementException:
                    gegründet = -1

                try:
                    rechtsform = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Art"]//following-sibling::*').text
                except NoSuchElementException:
                    rechtsform = -1

                try:
                    branche = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Branche"]//following-sibling::*').text
                except NoSuchElementException:
                    branche = -1

                try:
                    industriezweig = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industriezweig"]//following-sibling::*').text
                except NoSuchElementException:
                    industriezweig = -1

                try:
                    umsatz = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Umsatz"]//following-sibling::*').text
                except NoSuchElementException:
                    umsatz = -1

                try:
                    konkurrenten = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Konkurrenten"]//following-sibling::*').text
                except NoSuchElementException:
                    konkurrenten = -1

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                hauptsitz = -1
                firmengröße = -1
                gegründet = -1
                rechtsform = -1
                branche = -1
                industriezweig = -1
                umsatz = -1
                konkurrenten = -1

                
            if verbose:
                print("Hauptsitz: {}".format(hauptsitz))
                print("Firmengröße: {}".format(firmengröße))
                print("Gegründet: {}".format(gegründet))
                print("Rechtsform: {}".format(rechtsform))
                print("Branche: {}".format(branche))
                print("Industriezweig: {}".format(industriezweig))
                print("Umsatz: {}".format(umsatz))
                print("Konkurrenten: {}".format(konkurrenten))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job-Titel" : job_titel,
            "Geschätztes Bruttogehalt" : geschätztes_bruttogehalt,
            "Stellenbeschreibung" : stellenbeschreibung,
            "Bewertung" : bewertung,
            "Firmenname" : firmenname,
            "Ort" : ort,
            "Hauptsitz" : hauptsitz,
            "Firmengröße" : firmengröße,
            "Gegründet" : gegründet,
            "Rechtsform" : rechtsform,
            "Branche" : branche,
            "Industriezweig" : industriezweig,
            "Umsatz" : umsatz,
            "Konkurrenten" : konkurrenten})
            #add job to jobs

        #Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('.//li[@class="next"]//a').click()
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
