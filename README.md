# Scraping and Analysis of the technologies stack for Python Vacancies

## Features
- Web Scraping: Use Selenium to extract information about vacancies from dou.ua.
- Data Analysis: Provides statistical analysis on the collected data.

## Installation

To clone this project from GitHub, follow these steps:

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where you want to clone the project.**
3. **Run the following commands:**
```shell
git clone https://github.com/MaxymChyncha/dou-vacancy-analyzer.git
python -m venv venv
source venv/bin/activate  #for Windows use: venv\Scripts\activate
```

4. **Install requirements:**

```shell
pip install -r requirements.txt
```

5. **Run the Web Scraping Script:**
```shell
python -m app
```

6. **Work with Data Analysis:**

Follow the instructions and execute each cell in the notebook sequentially to perform the analysis.

## Files Structure

- `data_analysis`: Package that contains Jupyter Notebook file for working with data analysis
- `data_parsing`: Package that contains modules for scrapping, parsing and writing data
- `app.py`: Module that contains application for running WebScraping script