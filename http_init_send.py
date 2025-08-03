import serial
import time
import json
import os

# command1='AT'
# command2='AT+CGATT=1'
# command3='AT+CSTT="airtelgprs.com"'
# command4='AT+CIICR'
# command5='AT+CIFSR'
# ping_command_1='AT+CIPPING="www.google.com"'


path_to_folder ="C:\Users\Pavan G\Desktop\main_code"

with open(path_to_folder,'rb') as file:
  pass

def send_at(cmd,delay):
    ser.write((cmd+'\r\n').encode())
    time.sleep(delay)
    print(f'->{ser.read_all().decode()}\n')

def send_data_fn(cmd,delay):
    ser.write((cmd+'\r\n').encode())
    time.sleep(delay)
    response=ser.read_all().decode()
    print(f'->{ser.read_all().decode()}\n')
    return response



ser=serial.Serial('/dev/serial0',baudrate=9600,timeout=1)

# send_at('AT',delay=1)
send_at('AT+CPIN?',delay=1)         ## Just the Initialization Part
# send_at('AT+CSQ',delay=1)
# send_at('AT+CREG?',delay=1)           

send_at('AT+SAPBR=3,1,"CONTYPE","GPRS"',delay=1)
send_at('AT+SAPBR=3,1,"APN","airtelgprs.com"',delay=1)
send_at('AT+SAPBR=1,1',delay=1)
send_at('AT+SAPBR=2,1',delay=1)

send_at('AT+HTTPTERM',delay=2)  #closing http connection  before initiazlizing http 
send_at('AT+HTTPINIT',delay=1)

send_at('AT+HTTPPARA="CID",1',delay=1)
send_at('AT+HTTPPARA="URL","http://172.105.41.167/apiv4/devrawdataupload_ev.php"',delay=1)
send_at('AT+HTTPPARA="CONTENT","application/json"',delay=1)

data_json={
    
    "Device": "SIM800L"

    }

data_json_bytes=json.dumps(data_json).encode('utf-8')
print(f'No of elements:{len(data_json)} || Bytes:{len(data_json_bytes)}')
res=send_data_fn(f'AT+HTTPDATA={len(data_json_bytes)},1000',delay=2)

if "DOWNLOAD" in res:
    ser.write(data_json_bytes)
    time.sleep(5)
    print("Write is done")
    print(ser.read_all().decode())
    


send_at('AT+HTTPACTION=1',delay=5)                  # send a post request
send_at('AT+HTTPTERM',delay=2)                      # Terminate Connection
send_at('AT+SAPBR=0,1',delay=1)                     #

ser.close() 