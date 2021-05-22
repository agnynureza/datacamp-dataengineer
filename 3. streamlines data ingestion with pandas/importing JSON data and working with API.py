""" Introduction to JSON """
death_causes = pd.read_json("file you want to read",
                           orient="split") # ini penting

# soalnya bentuk json itu redundant, jadi klu dibikin column-oriented , biar enak dirubah ke dataframenya 


""" Introduction to APIs """
request.get("url string",
            params = "",
            headers="") 
#params
#headers, untuk auth
 
response.json() #return a dictionary
#pd.read_json("expected string not dictionary")
# jadi pake pd.DataFrame("dictionary")

headers = {"Authorization": "Bearer {}".format(api_key)} # untuk format string

bookstores = pd.DataFrame(data["bussiness"])


""" Working With Nested JSON """
from pandas.io.json import json_normalize

#json_normalize("dictionary") submodules dari pandas, gunanya buat flatten nested json 

bookstores = json_normalize(data["businesses"],
                            sep="_")
print(list(bookstores))
#["alias", "coordinates_latitude"]

#Deeply nested data 
json_normalize()
reacord_path # string/list of string attributes to nested data
meta #
meta_prefix


""" Combining Multiple Datasets """
1.
append("variable want to append",
       ignore_index=True)

2. Merge
#combining dataset to add related columns
merged = call_count.merge(weather,
                          left_on="created_date",
                          right_on="date")


""" Recap """

#chapter 1 dan 2 
read_csv()
read_excel()

#chapter 3 
read_sql()

#chapter 4
read_json()
json_normalize
requests


