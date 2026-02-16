from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator


# 1. usando preset @daily
with DAG(
    dag_id="02-define-scheduler-with-presets",
    start_date=datetime(2024, 9, 6),
    schedule="@daily",
    end_date=datetime(2030, 9, 6),
) as dag:

    task1 = EmptyOperator(task_id="extract")
    task2 = EmptyOperator(task_id="transform")
    task3 = EmptyOperator(task_id="load")

    task1 >> task2 >> task3


# 2. usando CRON
with DAG(
    dag_id="02-define-scheduler-with-crontab-expression",
    start_date=datetime(2024, 9, 6),
    end_date=datetime(2030, 9, 6),
    schedule="0 0 * * *",
) as dag:

    task1 = EmptyOperator(task_id="extract")
    task2 = EmptyOperator(task_id="transform")
    task3 = EmptyOperator(task_id="load")

    task1 >> task2 >> task3
