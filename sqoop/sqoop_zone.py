from datetime import datetime, timedelta
from textwrap import dedent
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow import DAG





default_args = {
    'owner': 'Apache_Sqoop_Zone',
    'depends_on_past': False,
    'email': ['sanjay.sheel@47billion.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
}




dag = DAG(dag_id='Sqoop_Zone',
          default_args=default_args,
          schedule_interval='50 7 * * *',
          )





task1_command = 'cd /home/sqoop_script_nyc/zone/ && sh sqoop_zone.sh '




task1 = SSHOperator(
    ssh_conn_id='ssh_default',
    task_id='Sqoop_Zone',
    command=task1_command ,
    dag=dag)




task1 