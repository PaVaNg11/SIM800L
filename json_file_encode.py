import json
import os
import base64



path_to_folder ="C:\\Users\\Pavan G\\Downloads\\Dyno data's\\Dyno data's\\Roll-000423\\Roll-[3]-000423.me"
 
with open(path_to_folder,'rb') as file:
    contents=file.read()


encoded=base64.b64encode(contents).decode()


json_data={"File_name":encoded}

json_data_bytes=json.dumps(json_data).encode()
print(len(json_data_bytes))