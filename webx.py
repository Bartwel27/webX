import sys
sys.path.insert(1,"assets/")

import fun
from fun import *

logo=fun._logo_("assets/logo.txt")
json_files = ["assets/data.json"]

with open(json_files[0]) as f:
	data = json.load(f)
pro_name = colored(data["system"]["name"],"red")
pro_ver = colored(data["system"]["ver"], "green")
pro_link = colored(data["system"]["dev"], "yellow")
print(f"""
  \t{logo}
       name: {pro_name}
       version: {pro_ver}
       developer: {pro_link}
""")
op_list = """
  [01] mkdir static project
  [02] mkdir dynamic project
  [03] laravel project
  [04] django project
  
  [05] update a project
  [06] upgrade a project
     		
"""
print(op_list)

