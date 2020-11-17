import re

str1 = """Interface		IP-Address	OK? 	Method Status	Protocol
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down"""
print("\n\n")
for line in str1.splitlines():
    mobj = re.match(r"(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+\w+", line, re.M | re.I)
    if mobj:
        print(mobj.group(1), ",", mobj.group(2), "\n")
print("\n\n")