from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="04-backfilling",
    start_date=datetime(2024, 7, 10),
    schedule="@daily",
    catchup=True
) as dag:

    task1 = EmptyOperator(
        task_id="extract"
    )

    task2 = EmptyOperator(
        task_id="transform"
    )

    task3 = EmptyOperator(
        task_id="load"
    )

    task1 >> task2 >> task3
