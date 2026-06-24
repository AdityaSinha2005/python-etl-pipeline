import glob
import pandas as pd  #python -m pip install pandas numpy
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt" 
target_file = "transformed_data.csv" 

#EXTRACT
def extract_from_csv(path):
    dataframe=pd.read_csv(path)
    return dataframe

def extract_from_json(path):
    dataframe=pd.read_json(path,lines=True) #lines=True as to enable JSON line format
    return dataframe

def extract_from_xml(path): 
    dataframe = pd.DataFrame(columns=["name", "height", "weight"]) #empty dataframe
    tree = ET.parse(path) #it loads XML to memory
    root = tree.getroot() 
    for person in root: 
        name = person.find("name").text 
        height = float(person.find("height").text) 
        weight = float(person.find("weight").text) 
        dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True) 
    return dataframe 


def extract(): 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
    
    for csvfile in glob.glob("data/*.csv"):   # process all csv files, except the target file
        if csvfile != target_file:  # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    for jsonfile in glob.glob("data/*.json"): # process all json files  
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    for xmlfile in glob.glob("data/*.xml"): # process all xml files 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 


#TRANSFORM

def transform(data): 
    
    data['height'] = round(data.height * 0.0254,2) #inches to meters
 
    data['weight'] = round(data.weight * 0.45359237,2)  #pounds to kg
	
    return data 

#LOADING AND LOGGING

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file) #transformed_data eak dataframe object hai


def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S'  
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 

 
log_progress("ETL process Started") 
 
log_progress("Extract phase Started") 
extracted_data = extract() 
  
log_progress("Extract phase Ended") 
 
log_progress("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
 
log_progress("Transform phase Ended") 
  
log_progress("Load phase Started") 
load_data(target_file,transformed_data) 
 
log_progress("Load phase Ended") 
 
log_progress("ETL Job Ended") 
