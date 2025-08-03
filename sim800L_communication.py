import serial
import time

command1='AT'
command2='AT+CGATT=1'
command3='AT+CSTT="airtelgprs.com"'
command4='AT+CIICR'
command5='AT+CIFSR'
ping_command_1='AT+CIPPING="www.google.com"'


def ping_ip(ping_time_duration,ping_command):
	start=time.time()
	
	while (time.time()-start <ping_time_duration):
		try:
			ser.write((f'{ping_command}\r\n').encode())
			time.sleep(2)
			print(ser.read_all().decode())
			
		except KeyboardInterrupt:
			print("\nDone pinging...")
			break

ser=serial.Serial('/dev/serial0',baudrate=9600,timeout=1)

ser.write((f'{command1}\r\n').encode())
time.sleep(1)
print(ser.read_all().decode())

ser.write((f'{command2}\r\n').encode())
time.sleep(1)
print(ser.read_all().decode())

ser.write((f'{command3}\r\n').encode())
time.sleep(1)
print(ser.read_all().decode())

ser.write((f'{command4}\r\n').encode())
time.sleep(2)
print(ser.read_all().decode())

ser.write((f'{command5}\r\n').encode())
time.sleep(1)
print(ser.read_all().decode())

#ping_ip(ping_time_duration=10,ping_command=ping_command_1)
time.sleep(1)
######################## Requesting Data ########################## 
ser.write(('AT+CIPSTART="TCP","thingspeak.mathworks.com",80\r\n').encode())
time.sleep(1)
print(ser.read_all().decode())
#ser.write(('AT+CIPSEND=63\r\n').encode())
#time.sleep(1)
print(ser.read_all().decode())
ser.write(('GET https://api.thingspeak.com/channels/2985929/status.json?api_key=SS16ZK7FCTD36Z6P \r\n\r\n').encode())
time.sleep(2)
print(ser.read_all().decode())
ser.write(('AT+CIPSHUT\r\n').encode())
time.sleep(3)
print(ser.read_all().decode())
ser.close() 

