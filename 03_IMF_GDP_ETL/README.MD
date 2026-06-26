# 🌍 IMF GDP ETL Pipeline

## 📌 Project Overview

This project implements a complete **ETL (Extract, Transform, Load) pipeline** using Python. The pipeline extracts GDP data of countries from an archived Wikipedia page, transforms the extracted data by converting GDP values from **Million USD** to **Billion USD**, and loads the processed data into both a **CSV file** and an **SQLite database**. Finally, SQL queries are executed to analyze the stored data.

This project was completed as part of the **IBM Data Engineering Professional Certificate**.

---

## 🎯 Project Objective

The objective of this project is to automate the process of:

* Extracting GDP data from a web page.
* Cleaning and transforming the extracted data.
* Loading the processed data into multiple storage formats.
* Querying the database for countries with GDP greater than or equal to **100 Billion USD**.
* Logging every stage of the ETL pipeline.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* BeautifulSoup (bs4)
* Requests
* SQLite3
* Datetime

---

## 📂 Project Structure

```text
03_IMF_GDP_ETL/
│
├── etl_project_gdp.py
├── Countries_by_GDP.csv
├── .gitignore
└── README.md
```

---

## ⚙️ ETL Workflow

### 1️⃣ Extract

* Download HTML content from the archived Wikipedia page.
* Parse HTML using BeautifulSoup.
* Extract GDP data from the required table.
* Ignore rows with missing GDP values.
* Create a Pandas DataFrame.

---

### 2️⃣ Transform

* Remove commas from GDP values.
* Convert GDP values from **Million USD** to **Billion USD**.
* Round values to **2 decimal places**.
* Rename the GDP column appropriately.

---

### 3️⃣ Load

The transformed data is loaded into:

* CSV File
* SQLite Database (`World_Economies.db`)

---

### 4️⃣ Query

Execute SQL query to retrieve countries having GDP greater than or equal to **100 Billion USD**.

```sql
SELECT *
FROM Countries_by_GDP
WHERE GDP_USD_billions >= 100;
```

---

## 📊 Output

### CSV Output

```
Countries_by_GDP.csv
```

### SQLite Database

```
World_Economies.db
```

Database Table:

```
Countries_by_GDP
```

---

## 📝 Logging

The ETL pipeline records execution progress using timestamps.

Example log entries:

```
Starting ETL process

Data extraction complete.

Transformation complete.

Data saved to CSV.

SQL Connection initiated.

Data loaded into database.

Process Complete.
```

---

## ▶️ How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install requests beautifulsoup4 pandas numpy
```

Run the project

```bash
python etl_project_gdp.py
```

---

## 📚 Key Concepts Learned

* Web Scraping with BeautifulSoup
* Data Extraction
* Data Cleaning
* Data Transformation
* ETL Pipeline Design
* Pandas DataFrame Operations
* CSV File Handling
* SQLite Database Integration
* SQL Query Execution
* Logging using Python

---

## 🚀 Future Improvements

* Automatic scheduling using Apache Airflow
* Store data in PostgreSQL instead of SQLite
* Export data in JSON format
* Interactive dashboard using Power BI or Tableau
* Containerize the pipeline using Docker

---

## 👨‍💻 Author

**Aditya Sinha**

B.Tech Computer Science & Engineering

KIIT University

IBM Data Engineering Professional Certificate
