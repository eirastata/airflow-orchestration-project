from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def minha_tarefa():
    print("Airflow está funcionando!")

with DAG(
    dag_id="minha_primeira_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    tarefa_1 = PythonOperator(
        task_id="print_hello",
        python_callable=minha_tarefa
    )

    tarefa_1
