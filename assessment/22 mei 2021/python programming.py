#1. inherentance class

class AstroBody:
    description = 'Natural entity in the observable universe.'    

class Star(AstroBody):
    pass

sun = Star()

print(sun.description) #Natural entity in the observable universe.'

#2. merge 2 set

a = {1, 2, 3}
b = {4, 5, 6}

print(a.union(b)) #{1, 2, 3, 4, 5, 6}

#3. merge flat list 

new_games = ['Sagrada', 'Cathedral', 'Wingspan']
boardgames = ['Carcassonne', 'Hive']

boardgames.extend(new_games)

print(boardgames) #['Carcassonne', 'Hive', 'Sagrada', 'Cathedral', 'Wingspan']

#4. iteration with next and conditional 
x = (i for i in range(5))

print(next(x)) #0

#5.using dictionary method
d = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4
}

print(d["three"]) #3

#6. difference set a dan b
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
 
print(a.difference(b)) #{1,2}

#7. simpen list params, *args
def add_many(*args):
    s = 0
    for n in args:
        s += n
    print(s)

print(add_many(100, 50, 3)) #153

#8.looping iteration
lst = ['numpy', 'pandas', 'requests']

lst_gen = (pkg for pkg in lst)

print(next(lst_gen)) #"numpy"

#9. ngambil doc atau comment pas bikin function
def square(x):
    """Returns the square of the argument x"""
    return x*x

print(square.__doc__) #'Returns the square of the argument x'

#10. merubah tuple menjadi set
x = (1, 2, 3)
s = set(x)

print(s) #{1, 2, 3}

#11. one line merubah list lower menjadi upper
[x.upper() for x in ['hello', 'world']]

#['HELLO', 'WORLD']

#12. merubah variabel global 
this_var = 30

def func():
  global this_var
  this_var = 20
  print(this_var)
    
print(this_var)
func()
print(this_var)

# 30
# 20
# 20

#13. membuat class di python
class Building:
    
    def __init__(self, number):
        self.number = number

b = Building(245)

print(b.number) #245

#14. melanjutkan iterasi
for i in "hello":
    if i == "l":
        continue
    print(i) # h,e,o
    
#15. cara memanggil lambda function
x = lambda : "I know how to call this function."

x()
  