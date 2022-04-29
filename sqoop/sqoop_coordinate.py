from datetime import datetime, timedelta
from textwrap import dedent
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow import DAG





default_args = {
    'owner': 'Apache_Sqoop_CoOrdinate',
    'depends_on_past': False,
    'email': ['sanjay.sheel@47billion.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
}




dag = DAG(dag_id='Sqoop_coordinate',
          default_args=default_args,
          schedule_interval='0 10 * * *',
          )





task1_command = 'cd /home/sqoop_script_nyc/coordinates/ && sh sqoop_coordinates.sh '




task1 = SSHOperator(
    ssh_conn_id='ssh_default',
    task_id='Sqoop_coordinates',
    command=task1_command ,
    dag=dag)




task1 