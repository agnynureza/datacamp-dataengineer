""" Introduce airflow """

airflow run dag_id dag_name start_date

""" Airflow  DAG """
#directed acylic graphs

from airflow.models import DAG
from datetime import datetime

# Define the default_args dictionary
default_args = {
    'owner': 'reza',
    'email': 'rezaagny@gmail.com',
    'start_date': datetime(2020, 1, 20)
}

# Instantiate the DAG object
etl_dag = DAG('etl_workflow', default_args=default_args)

""" Airflow web interface """

untuk mengakses airflow web server: 
airflow webserver -p 9090

cli-worker

bashoperator 
pythonoperator 
simplehttpoperator