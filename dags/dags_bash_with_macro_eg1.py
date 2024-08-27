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
    
    bash_task_2 = BashOperator(
        task_id='bash_task_2'
        env={ 'START_DATE':'{{}}',
             'END_DATE':'{{}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )