from airflow.models import Variable
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator


MINHA_VARIAVEL = Variable.get("minha_variavel")
PASSWORD_DB = Variable.get("DB_PASSWORD_TEST")


def minha_funcao():
    print(f"Minha variável é: {MINHA_VARIAVEL}")
    print(f"Senha do banco é: {PASSWORD_DB}")


with DAG(
    dag_id="07-variable-ui",
    start_date=datetime(2024, 7, 10),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="task-01",
        python_callable=minha_funcao
    )
