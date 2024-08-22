import datetime
import pendulum

from airflow.models.dag import DAG

from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as gag:
    
    send_emil_task = EmailOperator(
        task_id='send_emil_task',
        to='moonhs3002@penta.co.kr',
        subject='airflow test',
        html_content='airflow test'
    )