import datetime
import pendulum

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as gag:
    #start_date:2주전월요일 end_date:2주전토요일
    bash_task_2 = BashOperator(
        task_id='bash_task_2',
        env={ 'START_DATE':'{{ (data_interval_start.in_timezone("Asia/Seoul") - macros.delattr.relativedelta.relativetelta(days=19)) | ds }}',
             'END_DATE':'{{ (data_interval_start.in_timezone("Asia/Seoul") - macros.delattr.relativedelta.relativetelta(days=14)) | ds }}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )