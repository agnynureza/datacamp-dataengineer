""" Airflow Operator """

from airflow.operator.bash_operator import BashOperator
example_task = BashOperator(task_id='bash_ex',
                            bash_command='echo 1',
                            dag=dag)

""" Airflow Task """
bitshift operator 

""" Additional Operator """
pull_file_task = PythonOperator(
    task_id='pull_file',
    # Add the callable
    python_callable=pull_file,
    # Define the arguments
    op_kwargs={'URL':'http://dataserver/sales.json', 'savepath':'latestsales.json'},
    dag=process_sales_dag
)

# Import the Operator
from airflow.operators.email_operator import EmailOperator

# Define the task
email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task

""" airflow scheduling """
default_args = {
  'owner': 'Engineering',
  'start_date': datetime(2019, 11, 1),
  'email': ['airflowresults@datacamp.com'],
  'email_on_failure': False,
  'email_on_retry': False,
  'retries': 3,
  'retry_delay': timedelta(minutes=20)
}

dag = DAG('update_dataflows', default_args=default_args, schedule_interval='30 12 * * 3')

Set the start date of the DAG to November 1, 2019.
Configure the retry_delay to 20 minutes. You will learn more about the timedelta object in Chapter 3. For now, you just need to know it expects an integer value.
Use the cron syntax to configure a schedule of every Wednesday at 12:30pm.