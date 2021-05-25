""" Using Context Manager """
with open("file.txt") as my_file:
    
    
open() does 3 things :
set up context by opening file 
let you run any code  you want on that file
remove context by closing

""" Context Manager """
2 cara untuk mendeskripsikan context manager 
1. class based -> __enter__()
2. function based 

ada 5 langkah untuk membuat context manager based on function
def my_context():
    #add any set up code you need
    yield -> signal keyword kind of function
    #add any teardown code you need 
    add @contextlib.contextmanager decorator 
    
""" Advanced topics """
context manager pattern