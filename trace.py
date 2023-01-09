import requests as req
import socket
import os
import webbrowser as web
import time
import json as j

os.system("clear")
os.system("toilet -f future --gay Msec Trace")
print ("\033[1;33m============================\033[0m")
print ("\033[1;33mCreate By ./RedSec\033[0m")
print ("\033[1;33mRemember Msec\033[0m")
print ("\033[1;33m============================\033[0m")
print
ip = input("\033[1;33mMasukan IP => \033[0m")
print
coba = req.get(f"http://ip-api.com/json/{ip}")
if coba.status_code ==200:
    data = j.loads(coba.text)
    print("\033[1;31m")
    if data ["status"] == "success":
     print ("Kota : ", data["city"])
    print ("Negara : ", data["country"])
    print ("Waktu : ", data["timezone"])
    print ("Isp : ", data["isp"])
    lokasi =  data["lat"] , data["lon"]
web.open_new(f"https://www.google.co.id/maps/@{lokasi}")
print("")

