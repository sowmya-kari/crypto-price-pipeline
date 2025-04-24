from extract import extract_crypto_prices
from transform import transform_data
from load import load_to_postgres

def run_pipeline():
    data = extract_crypto_prices()
    clean_data = transform_data(data)
    load_to_postgres(clean_data)
    print("Done. Data saved to DB!")

if __name__ == "__main__":
    run_pipeline()
