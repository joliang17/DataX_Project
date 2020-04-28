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
Skill_Set = ['R', 'Python', 'HTML', 'CSS', 'SQL']


for skill in Skill_Set:
    # %%
    # Get content
    source = requests.get("http://oskicat.berkeley.edu/search~S1/X?SEARCH=(" + str(skill) + "+language)&SORT=D")


    # %%
    # Transform to soup type
    soup = bs.BeautifulSoup(source.content, features='html.parser') 

    # %% [markdown]
    # # Locate to specific class

    # %%
    Vertical_Box = soup.find_all('span',class_="briefcitTitle")[:5]

    # %%
    BookInformation = pd.DataFrame(columns = ['BookName', 'Href'])

    # %%
    for block in Vertical_Box:
        Href = 'http://oskicat.berkeley.edu' + block.a['href']
        BookName = block.text.replace('\n', '')
        BookList = [BookName, Href]
        BookList = pd.Series(BookList, index = BookInformation.columns)
        BookInformation = BookInformation.append(BookList, ignore_index=True)
    BookInformation


# %%
    dir_path = os.path.dirname(os.path.realpath(__file__))
    BookInformation.to_csv(os.path.join(dir_path, "BookInformation_" + skill + ".csv"))
    # BookInformation.to_csv("BookInformation_R.csv")


# %%


