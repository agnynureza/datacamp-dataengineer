""" Efficiently combining, counting and iterating """

pokemon = ['charmender', 'bulbasor', 'squirtle']
hp = [100,80,90]

#instead looping and enumerate we can use zip
combined_zip = zip(pokemon, hp)
# [("charmender", 100), . . . .]

#counting with loop
from collection import Counter

# 720 total
poke_types = ["Grass", ... , ...]
type_count = Counter(poke_types)

print(type_count) # key - values pair 
#Counter({"Grass": 10}, .... )

#combination or permutation
from itertools import combinations

poke_types = ["Bug", "Fire", ...]
combos_obj = combinations(poke_types, 2)

print([*combos_obj])
#[('bug', 'Fire'), ...] 

""" Set Theory """

intersection() # element yang ada di dua2nya 
union() # ngegabungin semua element yang ada di dua element
difference() # element yang ada di sebelah kiri cmn gk ada disebelah kanan
symmetric_difference() # semua element yang ada di 1 set doank

#negecheck pake IN
'Zubat' in {'bulbasor', 'Abra'} 

a = set("list")
b = set("list")
a.intersection(b) # bakal return apa yang ada di A dan di B
a.difference(b) # return perbedaaan apa yang di punya A tpi gk dipunya B
a.symmetric_difference(b) #return apa yang ada di A & tidak ada di B dan ada di B & tidak ada di A
a.union(b) #standar gabungin 2 set aja , cmn unique

""" Eliminating Loops """

#mempengaruhi waktu kecepatan response
poke_stats = [
    [90,92,39],
    [29,23,59]
]

#for loop approach 
totals = []
for row in poke_stats:
    total.append(sum(row))
    
#list comprehension 
total_comp = [sum(row) for row in poke_stas]

#build in func 
total_comp = [*map(sum, poke_stats)]

#atau bisa menggunaka numpy 
avgs = []
for row in poke_stats:
    avg = np.mean(row)
    avgs.append(avg)
print(avgs)

#lebih efektif dengan menggunakan built in dari numpy nya
avgs_np = poke_stats.mean(axis=1) #1 maksudnya tiap row

""" Writing Better Loops """

dengan pendekatan yang lebih holistik 
