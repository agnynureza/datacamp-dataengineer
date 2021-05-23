""" Intro Pandas Dataframe Iteration"""

#kita bisa menggunakan .iterrows() pada pandas klu pengen ngelooping data 
win_perc_list = []

for i, row in baseball_df.iterrows(): #pandas reseries

#klu bisa gk bisa iloc karena gk efficient

""" another iterator method: .itertuples() """
mengembalikan tipe data tuple yang bisa diacces dengan dot.
lebih efektif karena cara penyimpanan outputnya 


""" Pandas alternatif for looping """
apply() #apply in entire n dataframe 

#0 for column 
#1 for rows

lebih improve pake apply ternyata

""" Optimal Pandas iterating """
pada dasarnya pandas itu ada di bawah konsep nya numpy , jadi 
dengan baseball_df['W'].values -> ini menjadi numpy class