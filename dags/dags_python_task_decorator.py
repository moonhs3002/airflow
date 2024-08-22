
import pendulum

from airflow import DAG

from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="30 6 * * *",
     start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
):
    
    @task(task_id="python_task_1")
    def print_context(sum_input):
        print(sum_input)
        
    python_task_1 = print_context("task decorator run")
