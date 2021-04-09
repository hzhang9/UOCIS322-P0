"""
Complete credentials.ini, now after put that and hello.py in the same 
folder, being able to print "Hello World".
"""

import configparser
config = configparser.ConfigParser()
config.read("credentials.ini")

message = config["DEFAULT"]["message"]

print(message)
