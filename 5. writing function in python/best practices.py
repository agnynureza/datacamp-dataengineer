""" DocString """
untuk mempermudah penulisan func disarankan menggunakan docstring 
berupa """ """
apa saja yang di tulisa pada docstring 
#1.what function does ?
#2.what argument are ?
# 3. what return  value ?
# 4. info about any error raise ?
# 5. atau apaun yang ingin kamu katakan

import inspect
#berguna untuk informasi function
inspect.getdoc('function')

jadi cara bikin docstring
"""
def count_letter(content, letter):
    jelasin maksudnya function ini mau ngapain 

    Args:
        content(str): penjelasan
        letter(str): penjelasan 

    Returns: 
        int
        
    Raises:
        ValueError
"""

""" DRY and do one thing """
 Do one things 
 every function should one responsibility
 
 
""" Pass by assigment"""
jadi dalam python agak berbeda konsep immutable dan mutable nya jadi harus hati2