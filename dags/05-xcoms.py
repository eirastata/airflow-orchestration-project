from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract(ti):
    ti.xcom_push(key="primeiro_valor", value=10)
    ti.xcom_push(key="segundo_valor", value=20)


def transform(ti):
    primeiro_valor = ti.xcom_pull(key="primeiro_valor", task_ids="extract")
    segundo_valor = ti.xcom_pull(key="segundo_valor", task_ids="extract")

    print(f"XCOM são {primeiro_valor} e {segundo_valor}")


with DAG(
    dag_id="05-xcoms",
    start_date=datetime(2024, 8, 11),
    schedule=None,
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    task2 = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    task1 >> task2
