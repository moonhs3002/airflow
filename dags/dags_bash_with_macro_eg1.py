import datetime
import pendulum

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    
    python_t1 = PythonOperator(
        task_id = 'python_t1',
        python_callable=python_function1,
        op_kwargs={'start_date':'{{data_interval_start.in_timezone("Asia/Seoul")  | ds}}', 'end_date':'{{data_interval_end.in_timezone("Asia/Seoul")  | ds}}'}
    )

    #start_date:전월말일 end_date:1일전
    bash_task_1 = BashOperator(
        task_id='bash_task_1',
        env={'START_DATE':'{{ data_interval_start.in_timezone("Asia/Seoul") | ds}}',
             'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=1)) | ds }}'
        },
        bash_command='echo "data_interval_start: $START_DATE" && echo "END_DATE: $END_DATE"'
    )
    
    python_t1 >> bash_task_1