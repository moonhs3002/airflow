import datetime
import pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from airflow.decorators import task_group
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id="dags_python_with_task_gropu",
    schedule=None,
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    def inner_func(**kwargs):
        msg = kwargs.get('msg') or ''
        print(msg)

    @task_group(group_id= 'first_group')
    def group_1():
        '''task_group first group'''

        @task(task_id = 'inner_function1')
        def inner_function1(**kwargs):
            print('first group 1 task no.1')

        inner_function2 = PythonOperator(
            task_id = 'inner_function2',
            python_callable = inner_func,
            op_kwargs = {'msg':'first group task no.2'}
        )

        inner_function1() >> inner_function2
    
    with TaskGroup(group_id = 'second_group', tooltip = 'second group') as group_2:
        '''요긴 표시?'''
        @task(task_id = 'inner_function1')
        def inner_function1(**kwargs):
            print('second_group group 1 task no.1')

        inner_function2 = PythonOperator(
            task_id = 'inner_function2',
            python_callable = inner_func,
            op_kwargs = {'msg':'second group task no.2'}
        )

        inner_function1() >> inner_function2
    
    group_1() >> group_2

