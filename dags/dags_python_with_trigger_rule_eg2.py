import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException
from airflow.decorators import task

with DAG(
    dag_id="dags_python_with_trigger_rule_eg2",
    schedule=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    @task.branch(task_id = 'branching')
    def random_branch():
        import random
        item_lst = ['A','B','C']
        selected_item = random.choice(item_lst)

        if selected_item == 'A':
            return 'task_a'
        elif selected_item =='B':
            return 'task_b'
        elif selected_item =='C':
            return 'task_c'

    task_a = BashOperator(
        task_id = 'task_a',
        bash_command = 'echo upstream1'
    )

    @task(task_id = 'task_b')
    def task_b():
        print('b 정상')
    
    @task(task_id = 'task_c')
    def task_c():
        print('c 정상')

    @task(task_id = 'task_d', trigger_rele = 'none_shipped')
    def task_d():
        print('d 정상')

    random_branch() >> [task_a, task_b(), task_c()] >> task_d()

