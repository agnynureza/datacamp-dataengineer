""" Examining Runtime """

#magic command before the line code
import numpy as np 

%timeit rand_nums = np.random.rand(1000)

#%timeit harus di runningnya di python sheel
#kita bisa nyimpen hasil %timeit pada variable 
times = %timeid -o rand_nums = np.random.rand(1000)

times.timings
times.best
times.worst

buat ngecheck linenya banyak bisa pakai 
%%timeit dan di shell yah


""" Code Profiling for runtime """
pip install line_profiler 
#gunanya untuk melihat performace setiap baris code, klu %tiemit cmn result akhir
#jadi gk tau specific perform nya ada di line code yang mana

%load_ext line_profiler

%lprun -f name_function name_function(params)
#-f buat function


""" Code Profiling Memory Usage """
pip install memory_profiler

%load_ext memory_profiler

%mprun -f name_function name_function(params)

#func must be import whe using memory_profiling
from hero_func import convert_units

jadi ada pertimbangan antara kecepatan proses dan memory yang di pakai 

bisa dibandingkan dengan memakai 

line_profiler 
memory_profiler