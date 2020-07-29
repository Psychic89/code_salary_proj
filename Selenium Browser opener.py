#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:21:38 2020

@author: Robert
"""
import glassdoor_scraper as gs
import pandas as pd

path = "/Users/Robert/github/code_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 430, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)