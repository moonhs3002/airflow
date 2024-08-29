import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.decorators import task
from airflow.operators.email import EmailOperator

with DAG(
    dag_id="dags_python_email_xcom",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task(task_id = 'something_task')
    def some_logic(**kwarg):
        from random import choice
        return choice(['Success','Fail'])
    
    send_email = EmailOperator(
        task_id = 'send_email',
        to = 'moonhs3002@penta.co.kr',
        subject= '{{ data_interval_end.in_timezone("Asis/Seoul") | ds }} some_logic 처리',
        html_content = '{{ data_interval_end.in_timezone("Asis/Seoul") | ds }} 처리결과 <br> \
            {{ ti.xcom_pull(task_ids = "something_task")}} 했습니다. <br>'
    )

    some_logic() >> send_email