# Apache Airflow Orchestration Project

This repository contains my hands-on practice with **Apache Airflow**, focusing on workflow orchestration concepts used in **Data Engineering pipelines**.

The project demonstrates how to create, schedule, and manage DAGs, exchange data between tasks, and use Airflow Variables for dynamic configuration.

This project is part of my portfolio as I transition into the **Data Engineering field**.

---

# Technologies Used

* Apache Airflow
* Python
* Docker
* Astro CLI
* PostgreSQL

---

# Project Structure

```
dags/

02-define-scheduler.py

03-python-operator-args.py

04-backfilling.py

05-xcoms.py

06-xcom-return.py

07-variable-ui.py

08-variable-json.py
```

Each DAG demonstrates a specific Airflow concept.

---

# Concepts Demonstrated

## DAG Creation

Defines workflows and task dependencies.

Example:

```python
with DAG(
    dag_id="example",
    start_date=datetime(2024, 1, 1),
    schedule=None
):
```

---

## PythonOperator

Executes Python functions as Airflow tasks.

Example:

```python
PythonOperator(
    task_id="task_01",
    python_callable=minha_funcao
)
```

---

## XCom (Cross Communication)

Allows tasks to exchange data.

Example:

```python
ti.xcom_push(key="name", value="Tamine")
```

---

## Airflow Variables (UI)

Stores dynamic values in Airflow.

Example:

```python
Variable.get("nome")
```

---

## JSON Variables

Stores structured configuration.

Example:

```python
Variable.get("meu_json", deserialize_json=True)
```

---

## Backfilling

Allows execution of past scheduled runs.

---

# How to Run Locally

Using Astro CLI:

```bash
astro dev start
```

Then access Airflow UI:

```
http://localhost:8080
```

---

# Purpose of This Project

This repository demonstrates my practical knowledge of:

• Workflow orchestration
• Apache Airflow fundamentals
• Task scheduling
• Data exchange between tasks
• Dynamic pipeline configuration

---

# Example Output

Example log output from JSON Variable DAG:

```
Name: Tamine
City: São Paulo
Profession: Data Engineer
```

---

# Author

Tamine Eiras

Brazil

Aspiring Data Engineer

---

# Portfolio Project

This project is part of my Data Engineering portfolio.
