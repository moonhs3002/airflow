import datetime
import pendulum

from airflow.models.dag import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup=False
) as DAG:
    
    bash_orange = BashOperator(
        task_id="bash_orange",
        bash_command="/opt/airflow/plugins/select_fruit.sh ORANGE"
    )

    bash_avocado = BashOperator(
        task_id="bash_avocado",
        bash_command="/opt/airflow/plugins/select_fruit.sh AVOCADO"
    )

bash_orange >> bash_avocado