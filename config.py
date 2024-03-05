# Global Variables
# units_dict ={'height':'m', 'perimeter':'m', 'shgl':'m/s', 'velocity':'m/s', 'radius':'m', 'discharge':'m^3/sec', 'width':'ft',  'area':'m**2'}
parameters = ["height", "perimeter", "shgl", "radius", "velocity", "discharge", "width", "area"]
units = ["m", "m", "m/s", "m/s", "m", "m^3/hr", "m", "m^2"]
units_dict = dict(zip(parameters, units))
analyzers = ["analyzer_829", "analyzer_825", "analyzer_823"]
width = 2.7
manningcoefficent = 0.022
shgl = 0.005   # slope of hydralic grade line
baud_rate = 9600


site_id = "site_2982"
plant_name = "M/s. National Aluminium Company Limited,(NALCO)Smelter Plant"
plant_address1 = "Angul Angul"
plant_address2 = "759145 Odhisa"
plant_country = "India"
version = "ver1.0"

station_name = "Inlet-02"  #wit--->Water Inlet Tank
iso_latitude = "20.8653"
iso_longtitude = "85.1842"
fsw = site_id+"_"+station_name+"_"
comport = "/dev/ttyUSB0"

# Grewal AES key
AES256_KEY = "c2l0ZV8yOTgyXnZlcl8xLjBeT1NQQ0Je"

# Site Sunjray Public Key
site_public_key = "MEgCQQCJNEhkm8h3Amcq8MtGM8YalBFP4jA0H1UP/KmnnGzTvwxScHMR2oYveZmP\n4vtCMqIXqLSVifRFZNhdSlGBPd4RAgMBAAE="

# OSPCB Server Public Key
server_public_key = "MEgCQQCcADcRmHrTtDWsknzx5D64iNdwYscWi0+fI8nh9cO26HtRSeXBnSJuMlJK\nis7qn+lznsbi3DRwYOdM4w/7Z8bhAgMBAAE="

# Site private key
site_private_key = "MIIBPQIBAAJBAIk0SGSbyHcCZyrwy0YzxhqUEU/iMDQfVQ/8qaecbNO/DFJwcxHa\nhi95mY/i+0IyoheotJWJ9EVk2F1KUYE93hECAwEAAQJAblm0l+aLltxB6dF9TFs7\nzAim298J8gH5QkBumzY+By7HE2XYghGaVMlJKf76fVQJDuatKEfssOObVPKA3puu\n2QIjAI2hUFJhDMwxtKQ2Fzld9vAGUA/8AYte1FCchjUTVpw6mzcCHwD4AASqa1iZ\njUJr7ydadTK3brrDzB1iM5h8CM8ExPcCIwCLFZqSe7ocoMd7556g+JTzG8/uEpXV\nrzejPkNRxf7tB2S7Ah8AirIX6edXCalCuHJro99fmc7HjLEezcjlQpj6jkRJAiIs\n9kz5PqUTfoDFHUxf97zBqdP98pWofldeWOFjw1M/7yZE"

# IP Addresses
sunjray_hostAddress = "192.168.0.12:6410"
ospcb_hostAddress = "ospcb-rtdas.com"

# Sunjray Realtime and Delayed urls
sunjray_realtime_url = "http://192.168.0.12:6410/sunjrayServer/realtimeUpload"
sunjray_delayed_url = "http://192.168.0.12:6410/sunjrayServer/delayedUpload"

# OSPCB Realtime and Delayed urls
ospcb_realtime_url = "https://ospcb-rtdas.com/OSPCBRTDASServer/realtimeUpload"
ospcb_delayed_url = "https://ospcb-rtdas.com/OSPCBRTDASServer/delayedUpload"

# Required directories for project functioning
bkpdir = "BKPFLD"
cpcbdir = "CPCB"
spcbdir = "SPCB"

# Required directories in CPCB and SPCB for zipfile storing
rtdir = "Realtime"
dlydir = "Delayed"