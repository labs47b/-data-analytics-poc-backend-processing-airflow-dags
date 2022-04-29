from datetime import datetime, timedelta
from textwrap import dedent
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow import DAG





default_args = {
    'owner': 'Apache_Hive_create',
    'depends_on_past': False,
    'email': ['sanjay.sheel@47billion.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
}




dag = DAG(dag_id='Hive_table_create',
          default_args=default_args,
          schedule_interval='10 12 * * *',
          )





task1_command = 'cd /home/Apache_Hive && sh daily_trips.sh '




task1 = SSHOperator(
    ssh_conn_id='Hive_SSH',
    task_id='Hive_Table_creating',
    command=task1_command ,
    dag=dag)




task1 



