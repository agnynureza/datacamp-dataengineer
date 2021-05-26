""" working with templates """

using jinja templating language

templated_command=""" 
    echo "Reading {{ params.filename }}
""""

t1 = BashOperator(task_id='template_task',
                    bash_command=templated_command,
                    params={'filename': 'file1.txt'}
                    dag=example_dag)
                    
""" More Templates """

templated_command="""
    {% for filename in params.filenames %} 
    echo "Reading {{ filename }}"{% endfor %}
"""

t1 = BashOperator(task_id='template_task',   
                    bash_command=templated_command, 
                    params={'filenames': ['file1.txt', 'file2.txt']},   
                    dag=example_dag)
                    
Execution Date: {{ ds }}    # YYYY-MM-DD
Execution Date, no dashes: {{ ds_nodash }}            # YYYYMMDD
Previous Execution date: {{ prev_ds }}                # YYYY-MM-DD
Prev Execution date, no dashes: {{ prev_ds_nodash }}  # YYYYMMDD
DAG object: {{ dag }}Airflow config object: {{ conf }}


{{ macros.datetime }}:Thedatetime.datetimeobject
{{ macros.timedelta }}:Thetimedeltaobject{
{ macros.uuid }}:Pythons uuidobject
{{ macros.ds_add('2020-04-15', 5) }}:Modifydaysfromadate,
this example returns 2020-04-20

""" Branching """

using BranchPythonOperator
provide_context = true , buat ngebaca dsnya


""" Creating Production Pipeline """