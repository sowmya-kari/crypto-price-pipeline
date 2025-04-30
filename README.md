# 🚀 Crypto Price Pipeline

This project implements a basic **ETL pipeline** to extract cryptocurrency price data, transform it, and load it into a data store. The workflow is orchestrated using **Apache Airflow**.

## 🗂️ Project Structure

```
crypto_price_pipeline/
├── dags/
│   └── crypto_price_pipeline.py  # Airflow DAG definition
├── extract.py                    # Extracts data from a crypto API
├── transform.py                  # Cleans/transforms the extracted data
├── load.py                       # Loads the transformed data into a database or file
├── main.py                       # Entry point for manual runs or testing
└── README.md                     # Project documentation
```

## 🔄 ETL Process

### 1. **Extract**
- Implemented in `extract.py`
- Fetches current crypto price data from a public API like CoinGecko or CoinMarketCap

### 2. **Transform**
- Implemented in `transform.py`
- Cleans and reshapes the raw JSON data into a tabular format (e.g., Pandas DataFrame)

### 3. **Load**
- Implemented in `load.py`
- Loads the data into a local CSV file, database, or cloud storage (e.g., S3, BigQuery)

### 4. **Orchestration**
- The pipeline is orchestrated using **Apache Airflow**, defined in `dags/crypto_price_pipeline.py`

## 🛠️ Requirements

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

> Add your dependencies to a `requirements.txt` file, e.g., `pandas`, `requests`, `apache-airflow`.

## ▶️ Running the Pipeline

### Run with Airflow:
1. Start Airflow:
   ```bash
   airflow standalone
   ```
2. Access the Airflow UI at `http://localhost:8080`
3. Enable and trigger the DAG: `crypto_price_pipeline`

### Run Manually (for testing):
```bash
python main.py
```

## 📂 Output

The transformed and loaded data can be found in:
- `data/crypto_prices.csv` (or your target destination)

## ✅ TODO

- [ ] Add error handling and logging
- [ ] Support multiple crypto symbols
- [ ] Schedule hourly or daily DAG runs
- [ ] Add data validation steps

## 👩‍💻 Author

Created by [Sowmya Kari](https://github.com/sowmya-kari)
