import re
import os
import interface.inp as inp
from interface.inp import accesible
import subprocess


print(accesible())

def git_clone(url, directory):
    try:
        subprocess.check_output(["git", "clone", url, directory])
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
        

def read_files(directory):
   for filename in os.listdir(directory):
       if os.path.isfile(os.path.join(directory, filename)):
           str_data = filename.read()
           return str
   

def find_classes(inp):
    pattern = r'\b\w+\(.*?\)'
    matches = re.findall(pattern, inp)
    return matches

    
def find_funcs(inp):
    pattern = r'(?<=\b\w+\.)\w+\(.*?\)'
    matches = re.findall(pattern, inp)
    return matches




make_graph():
    (nest_level, func_name) = 

    

    