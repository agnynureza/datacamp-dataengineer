""" Introduction to spreadsheet """
import pandas as pd 

data = pd.read_excel("file want to read",
                     skiprows = "mulai dari row berapa" ,
                     usecols = "columns apa aja yang ditampilin")

data.head() #untuk ngeprint sample data (5 rows data teratas)
data.columns #untuk ngeprint column apa aja yang diambil


""" Getting data from multiple worksheets """
survey_data = pd.read_excel("file want to read",
                            sheet_name = "2017") #misal untuk baca sheet yang mana mau diambil

#problem ? bagaimana klu mau ambil semua sheet nya 
survey_data = pd.read_excel("file want to read",
                            sheet_name = None) # bisa berupa list juga or combination index or name

#putting all together
all_response = pd.DataFrame()

## iterate through data frames in dictionary 
for sheet_name, frame in survey_data.items():
    # add column so we know which year data is from
    frame["Year"] = sheet_name
    
    #add each data frame to all_response
    all_response = all_response.append(frame)

#check unique
print(all_response.Year.unique())

df.shape[0] #menghitung jumlah rows


""" Modifying imports: true/false data """
bootcamp_data = pd.read_excel("file want to read",
                              dtype :{}, #passing data dictionary
                              true_values = ["Yes"],
                              false_values = ["No"])


bootcamp_data.dtypes #untuk mengecheck data types dari columns yang diambil 
bootcamp_data.sum() # mengecheck jumlah data yang terisi pda setiap columns nya
bootcamp_data.isna().sum() # mengecheck berapa banyak data yang hilang tiap column nya 



""" Modifying import: parsing dates """
survey_df = pd.read_excel("file want to read",
                          parse_dates = [""]) # berupa list of string, column name yang mau di parse


#combine split coloumns 
date_cols = {
    "Part2Start" : ["Part2startDate", "Part2StartTime"] # can passing to parse_dates
}


format_string = "%m%d%Y %H%:%M:%S"

survey_df ["part2datetime"] = pd.to_datetime(surveydf["part2endtime"],
                                             format = format_string)

# mengecheck apakah yang di parse sudah benar 
survey_df."column".head() 