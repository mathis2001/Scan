import os

a=input("Veuillez entrer une IP (/24)\n")
IP=a.split(".")
IP.pop()
IPp=(".").join(IP)
for i in range(1,255):
	IPf=IPp+"."+str(i)
	resu=os.system("ping -c1 -W1  "+IPf+">/dev/null")
	if (resu==0):
		print("adresse IP connectée :",IPf)
	else:
		print("adresse IP non connectée :",IPf)
