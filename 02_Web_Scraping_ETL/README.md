# Web Scraping ETL Pipeline

## Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Python. The pipeline extracts movie ranking data from a web page, transforms the extracted information into a structured format using Pandas, and loads the processed data into both a CSV file and a SQLite database.

The project was built as part of my Data Engineering learning journey to gain hands-on experience with web scraping, data transformation, and database loading.

---

## Data Source

Movie ranking data is extracted from the following archived webpage:

https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films

The dataset contains information about highly ranked films, including:

* Average Rank
* Film Name
* Release Year

---

## Technologies Used

* Python
* Requests
* BeautifulSoup4
* Pandas
* SQLite3

---

## ETL Workflow

### 1. Extract

The pipeline sends an HTTP request to the target webpage and retrieves the HTML content.

```python
html_page = requests.get(url).text
```

BeautifulSoup is then used to parse the HTML document.

```python
data = BeautifulSoup(html_page, "html.parser")
```

---

### 2. Transform

The movie table is extracted from the webpage and converted into a Pandas DataFrame.

Extracted fields:

* Average Rank
* Film
* Year

The project processes only the top 50 movies from the source dataset.

Example DataFrame:

| Average Rank | Film          | Year |
| ------------ | ------------- | ---- |
| 1            | The Godfather | 1972 |
| 2            | Citizen Kane  | 1941 |
| 3            | Casablanca    | 1942 |

---

### 3. Load

The transformed dataset is stored in:

#### CSV File

```text
top_50_films.csv
```

#### SQLite Database

```text
Movies.db
```

Table Name:

```text
Top_50
```

---

## Project Structure

```text
02_Web_Scraping_ETL/
│
├── webscraping_movies.py
├── Movies.db
├── top_50_films.csv
└── README.md
```

---

## How to Run

### Install Dependencies

```bash
pip install pandas requests beautifulsoup4
```

### Execute the Script

```bash
python webscraping_movies.py
```

---

## Output

After successful execution:

* Movie data is scraped from the webpage.
* A Pandas DataFrame is generated.
* Results are exported to a CSV file.
* Data is loaded into a SQLite database.

---

## Learning Outcomes

Through this project, I practiced:

* Web Scraping with BeautifulSoup
* Data Extraction using Requests
* Data Transformation using Pandas
* CSV Data Export
* SQLite Database Operations
* ETL Pipeline Development

---

## Author

Aditya Sinha

B.Tech CSE | KIIT University

Learning Data Engineering, Backend Development, and Software Engineering.
