# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# make it run on py2 and py3
from __future__ import division, print_function


# %%
# stretch Jupyter coding blocks to fit screen
from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>")) 
# if 100% it would fit the screen

# %% [markdown]
# # Import Packages

# %%
import requests
import bs4 as bs
import pandas as pd
import re
import os 

# %% [markdown]
# # Connect to a website

Job_Title = ["Data Scientist", "Software Engineer", "Data Analyst", "Data Engineer", "Statistician", "DBA/Database Engineer", "Research Scientist", "Product/Project Manager", "Business Analyst"]

Job_Title_url = [job.replace(' ', '+') for job in Job_Title]

JobInformation = pd.DataFrame(columns = ['Job_Title', 'Salary', 'Skills', 'Href'])

# Get content
for Job_Index, Job in enumerate(Job_Title):

    url = "https://www.payscale.com/rcsearch.aspx?CountryName=United%2BStates&str=" + Job_Title_url[Job_Index]
    source = requests.get(url)
    soup = bs.BeautifulSoup(source.content, features='html.parser') 
    if soup.find('div', class_='job__description') == None:
        
        candidate_block = soup.find_all('div', class_='RCSearchCategoryResultsContainer')
        Candidate_Jobs = [block for block in candidate_block if "Top Results for Job" in str(block)]
        url = 'https://www.payscale.com' + Candidate_Jobs[0].find_all('li', class_='RCSearchCategoryResultListItem')[0].find('a')['href']

        
        source = requests.get(url)
        soup = bs.BeautifulSoup(source.content, features='html.parser') 


    # Get informations
    

    AvgSalary = soup.find('div', class_='job__description').text
    AvgSalary = re.findall(r"\$\d+\,?\d*", AvgSalary)[0]

    Job_link = soup.find('link', rel='canonical')['href']

    Vertical_Box = soup.find_all(class_='popular-skill__name')

    for block in Vertical_Box:
        Href = Job_link
        Job_Name = Job
        Salary = AvgSalary
        Skill = block.text
        JobList = [Job_Name, Salary, Skill, Href]
        JobList = pd.Series(JobList, index = JobInformation.columns)
        JobInformation = JobInformation.append(JobList, ignore_index=True)


dir_path = os.path.dirname(os.path.realpath(__file__))
JobInformation.to_csv(os.path.join(dir_path, "JobInformation.csv"))