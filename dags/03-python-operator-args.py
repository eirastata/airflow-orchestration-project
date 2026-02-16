from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# função 1
def primeira_funcao(valor):
    print(f"Minha primeira função recebeu: {valor}")


# função 2
def segunda_funcao(par1, par2):
    print(f"Minha segunda função recebeu: {par1} e {par2}")


with DAG(
    dag_id="03-python-operator-args",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # executa manualmente
    catchup=False
) as dag:

    tarefa1 = PythonOperator(
        task_id="primeira_funcao",
        python_callable=primeira_funcao,
        op_args=[10]
    )

    tarefa2 = PythonOperator(
        task_id="segunda_funcao",
        python_callable=segunda_funcao,
        op_kwargs={
            "par1": 20,
            "par2": 30
        }
    )

    tarefa1 >> tarefa2
