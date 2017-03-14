# Shodan_Raspi
###### ***Hack Raspberry Pi(s) across the world !***  
   
   
This script basically uses `shodan` api to search Raspberry Pi's ip addresses , and tries to `ssh` into them by using the default username: ***pi*** and password: ***raspberrry***, and stores the successful ip addresses into a  text file.  

##Usage:  
```python
user@pc:~$python shodan_raspi.py [source_file_name]
``` 
If the source file doesn't exist , it'll be created, using `Shodan` api.  
The Source File consists of ip address, only one per line.  
Setup your `Shodan` api key in the script.  
