# Job Recommendation System (Data-X Project)

(Project brief)

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

1. Download project code package from Github.

2. Install necessary Python packages.

    - Change the current working directory to this project folder, and install packages with the specific version in [`requirements.txt`](requirements.txt) through command line.

        ```bat
        cd DataX_Project
        pip install -r requirements.txt
        ```

3. Start the Python program for web page.
   - Change the current working directory to the core [`app.py`](WebSites/Webpage_Final/app.py) file under `Webpage_Final` folder, and run this file through command line.

        ```bat
        cd WebSites/Webpage_Final
        python app.py
        ```

   - If successfully start the program, click (or type?) the url address in the web brower that shows in the command line.

        ```
        http://127.0.0.1:8000/
        ```

   - Enter your basic information, and generate your own recommended result :laughing: ! (See in demo video)
  
   - Finally, use `Ctrl + C` to stop the program in commend line.

> data cleaning part?

> model selection?

## Reference

This part includes all the external codes and materials we referred to.

- [data-x Github repository](https://github.com/ikhlaqsidhu/data-x)
- [HTML Tutorial](https://www.w3schools.com/html/)

## Project Links

- Project Presentation Slide
- Write-up
- Demo video
