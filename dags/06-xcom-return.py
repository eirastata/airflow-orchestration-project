from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Task 1
def extract():

    valor = 10

    return valor


# Task 2
def transform(ti):

    valor_recebido = ti.xcom_pull(task_ids="extract")

    print(f"O valor recebido foi: {valor_recebido}")


with DAG(

    dag_id="06-xcom-return",

    start_date=datetime(2024, 8, 11),

    schedule=None,

) as dag:


    task1 = PythonOperator(

        task_id="extract",

        python_callable=extract,

    )


    task2 = PythonOperator(

        task_id="transform",

        python_callable=transform,

    )


    task1 >> task2
