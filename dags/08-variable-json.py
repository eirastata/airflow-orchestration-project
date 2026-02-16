from airflow.models import Variable
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator


MEU_JSON = Variable.get("meu_json", deserialize_json=True)


def minha_funcao():

    print(f"Nome: {MEU_JSON['nome']}")
    print(f"Cidade: {MEU_JSON['cidade']}")
    print(f"Profissão: {MEU_JSON['profissao']}")


with DAG(
    dag_id="08-variable-json",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="task_01",
        python_callable=minha_funcao
    )
