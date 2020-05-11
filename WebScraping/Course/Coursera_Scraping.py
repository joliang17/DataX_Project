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
import os

# %% [markdown]
# # Connect to a website

# %%
Skill_Set = ['R', 'Python', 'HTML', 'CSS', 'SQL', 'Java', 'Julia', 'Scala', 'MATLAB', 'C', 'C++']


for skill in Skill_Set:
    # %%
    # Get content
    source = requests.get("https://www.coursera.org/search?query=" + skill)


    # %%
    # Transform to soup type
    soup = bs.BeautifulSoup(source.content, features='html.parser') 

    # %% [markdown]
    # # Locate to specific class

    # %%
    Vertical_Box = soup.find_all('li',class_="ais-InfiniteHits-item")[:10]


    # %%
    CourseInformation = pd.DataFrame(columns = ['CourseName', 'Rating', 'ClassDifficulty', 'PartnerName', 'Href'])
    CourseInformation


    # %%
    for block in Vertical_Box:
        Href = 'www.coursera.org' + block.find('a')['href']
        CourseName = block.find(class_="color-primary-text card-title headline-1-text").text
        Rating = block.find(class_="ratings-text").text
        ClassDifficulty = block.find(class_="difficulty").text
        PartnerName = block.find(class_="partner-name").text
        CourseList = [CourseName, Rating, ClassDifficulty, PartnerName, Href]
        CourseList = pd.Series(CourseList, index = CourseInformation.columns)
        CourseInformation = CourseInformation.append(CourseList, ignore_index=True)
    CourseInformation


    # %%
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CourseInformation.to_csv(os.path.join(dir_path, "Data\CourseInformation_" + skill + ".csv"))
    # CourseInformation.to_csv("CourseInformation_" + skill + ".csv")


    # %%


