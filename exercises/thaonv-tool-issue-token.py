import time
import os

try:
    t = float(input('Enter time that you want to issue token (in minutes): '))
except:
    print('Please enter a number!')
    t = float(input('Enter time that you want to issue token (in minutes): '))
    
os.environ["OS_USERNAME"] = "admin"
os.environ["OS_PASSWORD"] = "Welcome123"
os.environ["OS_AUTH_URL"] = "http://192.168.100.40:5000/v2.0"
os.environ["OS_TENANT_NAME"] = "admin"
os.environ["OS_REGION_NAME"] = "RegionOne"

t_end = time.time() + 60 * t

while time.time() < t_end:
    os.system("openstack token issue")
print('Complete')    