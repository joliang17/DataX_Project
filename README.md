# A Job Recommendation System (Data-X Project)

Contributors: Cheng-chun Chao, Sean Chuang, Xinyu Wang, Yijun Liang, Yuanyuan Xiao

## Project Brief

Job hunting can be quite frustrating, and it is not just about an eye-catching resume.  You need to know how your knowledge level locates you in the job experience level, what kind of extra skills you need to master, also you would like to know the appropriate salary range for the job you are looking for so you can negotiate with HR for a better offer.

In order to help out, the team built a corresponding recommendation engine, where users provide their basic information and the website will return suggested jobs and other related information such as salary, needed skills, and useful courses/books.

This application specifically targets people who lack job searching experience, for example, fresh graduates. Its recommendation engine can help them understand based on their current skills set, what kind of jobs fits users, and what’s the reasonable range of salary for them to ask during offer negotiating. Additionally, it can also help HR who would like to recruit talents and see what necessary skills they need to screen for the candidate’s resumes.

This readme file mainly gives a brief introduction on how to make preparation and successfully run our job recommendation system.

## Prerequisites

```
Python 3.7
numpy 1.18.1
pandas 1.0.1
matplotlib 3.1.3
scikit-learn 0.22.1
joblib 0.14.1
flask 1.1.1
requests 2.22.0
beautifulsoup4 4.8.2
```

## Installation

1. Download project code package from Github, or `git clone` from GitHub.

     ```
     git clone https://github.com/joliang17/DataX_Project.git
     ```

2. Create a new virtual environment with Python 3.7, and activate it.

     ```bat
     conda create -n JobRecommendation python=3.7 anaconda
     activate JobRecommendation
     ```

3. Install necessary Python packages.

    - Open a new terminal,and change the terminal's current working directory to this downloaded project folder.
    - Install packages with the specific version in [`requirements.txt`](requirements.txt) through command line.

        ```bat
        cd DataX_Project
        pip install -r requirements.txt
        ```

4. Start the Python program for web page.
   - Change the current working directory to the core [`app.py`](WebSites/Webpage_Final/app.py) file under `Webpage_Final` folder, and run this file through command line.

        ```bat
        cd WebSites/Webpage_Final
        python app.py
        ```

   - If successfully start the program, Open the following url address in the web brower that shows in the command line.

        ```
        http://127.0.0.1:8000/
        ```

   - Enter your basic information, and generate your own recommended result :laughing: ! (See in demo video)
  
   - Finally, use `Ctrl + C` to stop the program in commend line.

## Reference

This part includes all the external codes and materials we referred to.

- [data-x Github repository](https://github.com/ikhlaqsidhu/data-x)
- [Python Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/)
- [HTML Tutorial](https://www.w3schools.com/html/)
- [CSS Tutorial](https://www.w3schools.com/css/)

## Project Links

- [Project Presentation Slide]()
- [Write-up report](Deliverables/Final%20Report.pdf)
- [INavigator](Deliverables/iNavigator.pdf)
- [Demo video]()
