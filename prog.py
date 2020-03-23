import subprocess
import time
import pandas as pd
import ml

time.sleep(1)
for i in range(1,100):

	#time.sleep(1)
	subprocess.call('timeout 1s tshark -i ens33 -w capture3.pcap',shell=True)
	subprocess.call('tshark -r capture3.pcap > output3.txt',shell=True)
	subprocess.call('rm capture3.pcap',shell=True)
	subprocess.call('python3 calculate_entropy.py',shell=True)
	
	with open('update','r') as f:
		x=f.read()
	#print("x=",x)
	if x == '1':
		with open('temp','r') as f:
			line = f.readline()
			line = line.strip()
			line = line.split(',')

			inp = { 'a':[float(line[0])], 'b':[float(line[1])], 'c':[float(line[2])], 'd':[float(line[3])], 'e':[float(line[4])]}
			inp = pd.DataFrame(inp)
			res = ml.lg.predict(inp)
		if str(res) == "[1]":
			subprocess.call('notify-send -i software-update-urgent "System Under DDOS Attack"',shell=True)
		#print("updated")
		with open('result.txt','a') as  f:
			f.write(str(res))
	#subprocess.call('ls',shell=True)
	with open('update','w') as f:
		f.write('0')
