#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:50:10 2020

@author: Robert
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')



#Remove salary column
df = df.drop('Geschätztes Bruttogehalt', axis = 1)



#Company name text only
df['firmenname_txt'] = df.apply(lambda x: x['Firmenname'] if x['Bewertung'] <0 else x['Firmenname'][:-3], axis = 1)


#Remove non-existent company names
df = df[df['Firmenname'] != 'nan']

#Remove rows without Hauptsitz

#Remove salary column
df = df[df['Hauptsitz'] != '-1']

#Country Field
df['job_country'] = df['Hauptsitz'].apply(lambda x: x.split(',')[1])

#City Field
df['job_city'] = df['Hauptsitz'].apply(lambda x: x.split(',')[0])
df.job_city.value_counts()

#Is the job at the company headquarters?
df['job_at_hq'] = df.apply(lambda x: 1 if x.Ort == x.job_city else 0 , axis = 1)

#Age of company
df['company_age']= df.Gegründet.apply(lambda x: x if x < 0 else 2020-x)

#Parsing of job description (python etc)
df['Stellenbeschreibung'][0]

#python
df['python_yn'] = df['Stellenbeschreibung'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()

#rstudio
df['R_yn'] = df['Stellenbeschreibung'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
df.R_yn.value_counts()

#spark
df['spark'] = df['Stellenbeschreibung'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark.value_counts()

#aws
df['aws'] = df['Stellenbeschreibung'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws.value_counts()

#excel
df['excel'] = df['Stellenbeschreibung'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel.value_counts()

#sql
df['Sql'] = df['Stellenbeschreibung'].apply(lambda x: 1 if 'sql' in x.lower() or 'mysql' in x.lower() else 0)
df.Sql.value_counts()

df_out = df.to_csv('jobs_data_cleaned.csv', index = False)

