from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime, timedelta
from extract import extract_crypto_prices
from transform import transform_data
from load import load_to_postgres

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}

with DAG(
    dag_id="crypto_price_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:

    create_table = PostgresOperator(
        task_id="create_crypto_table",
        postgres_conn_id="postgres_default",
        sql="sql/create_table.sql"
    )

    extract = PythonOperator(
        task_id="extract_crypto_data",
        python_callable=extract_crypto_prices
    )

    def _transform_and_load(**context):
        data = context["ti"].xcom_pull(task_ids="extract_crypto_data")
        records = transform_data(data)
        load_to_postgres(records)

    transform_and_load = PythonOperator(
        task_id="transform_and_load",
        python_callable=_transform_and_load,
        provide_context=True
    )

    create_table >> extract >> transform_and_load
