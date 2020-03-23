#file handling in python 
import math

c=0
with open('output3.txt','r') as f:   #context manager
	
	src_ip={}
	dst_ip={}
	src_port={}
	dst_port={}
	length={}

	for line in f:
		#line = line.split(',')
		line = line.strip()
		line = line.split(' ')
		#print(line)
		s_ip = line[1]
		d_ip = line[3]
		l = line[5]
		s_port = line[6]
		d_port = line[7]
		c+=1

		#storing source ip in dict
		if src_ip.get(s_ip) != None:
			src_ip[s_ip]+=1
		else:
			src_ip[s_ip]=1
		
		#storing destination ip in dict
		if dst_ip.get(d_ip) != None:
			dst_ip[d_ip]+=1
		else:
			dst_ip[d_ip]=1

		#storing length of packet
		if length.get(l) != None:
			length[l]+=1
		else:
			length[l]=1

		#storing source port in dict
		if src_port.get(s_port) != None:
			src_port[s_port]+=1
		else:
			src_port[s_port]=1

		#storing destination port in dict
		if dst_port.get(d_port) != None:
			dst_port[d_port]+=1
		else:
			dst_port[d_port]=1
	

entropy_src_ip=0
entropy_dst_ip=0
entropy_src_port=0
entropy_dst_port=0
entropy_length=0

if c>10:
	#source address entropy
	for keys,values in src_ip.items():
		p=values/c
		entropy_src_ip=entropy_src_ip-(p*math.log(p,2))

	#destination address entropy
	for keys,values in dst_ip.items():
		p=values/c
		entropy_dst_ip=entropy_dst_ip-(p*math.log(p,2))

	#length of packet entropy
	for keys,values in length.items():
		p=values/c
		entropy_length=entropy_length-(p*math.log(p,2))

	#source port entropy
	for keys,values in src_port.items():
		p=values/c
		entropy_src_port=entropy_src_port-(p*math.log(p,2))

	#destination port entropy
	for keys,values in dst_port.items():
		p=values/c
		entropy_dst_port=entropy_dst_port-(p*math.log(p,2))

	'''print('Source IP : ',entropy_src_ip)
	print('Destination IP : ',entropy_dst_ip)
	print('Length : ',entropy_length)
	print('Source Port : ',entropy_src_port)
	print('Destination Port : ',entropy_dst_port)'''

	#with open('normal.csv','a') as f:
	data = str(entropy_src_ip)+','+str(entropy_dst_ip)+','+str(entropy_src_port)+','+str(entropy_dst_port)+','+str(entropy_length)+'\n'
		#f.write(data)

	with open('temp','w') as f:
		f.write(data)

	with open('update','w') as f:
		f.write('1')
	#print("written")

