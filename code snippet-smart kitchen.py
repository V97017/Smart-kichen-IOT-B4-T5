import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#credentils
OrganizationID= "5yus9k"
DeviceType= "raspberry_pie"
DeviceID= "1956"
AuthenticationMethod= "token"
AuthenticationToken= "12345678"
#initialize GPIO

def myCommandCallback(cmd):
    print("command received: %s" %cmd.data)
    print(type(cmd.data))
try:
    deviceOptions={"org":OrganizationID,"type":DeviceType,"id":DeviceID,"auth-method":AuthenticationMethod,"auth-token":AuthenticationToken}
    deviceCli=ibmiotf.device.Client(deviceOptions)
#-------------
except Exception as e:
    print("caught exception connecting device:%s" %str(e))
    sys.exit()
#connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:

    jar1=random.randint(0,3000)
    jar2=random.randint(0,3000)
    jar3=random.randint(0,3000)
    # print(hum)
    cylinderweight=random.randint(0,25)
    gasleak=random.randint(0,10)
    #send Jars densities and Cylinder density and leakage density to IBM Watson
    data ={'CashewJarWeight':jar1,'PeanutJarWeight':jar2,'MilletsJarWeight':jar3,'CylinderWeight':cylinderweight,'GasLeakage':gasleak}
    #print(data)
    def myOnPublishCallback():
        print ("CashewJarWeight = %s grams" % jar1,"PeanutJarWeight = %s grams" %jar2,"MilletsJarWeight = %s grams" %jar3,"CylinderWeight = %s Kg"%cylinderweight,"GasLeakage = %s grams"%gasleak)
    

    success = deviceCli.publishEvent("IOT", "json", data, qos=0, on_publish=myOnPublishCallback)
    if(jar1<50):
        r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=RcIXU7uQ3HSYPhaeWLf0JkoGmbsF6w2rl9KAMtDqg5xTz48dBpn0kS7eNGOyZEdfwDKJQa8CXzLFPqR5&sender_id=FSTSMS&message=Cashew jar is going to be empty soon.Please get them.&language=english&route=p&numbers=9704207699')

        print(r.status_code)
    if(jar2<50):
        r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=RcIXU7uQ3HSYPhaeWLf0JkoGmbsF6w2rl9KAMtDqg5xTz48dBpn0kS7eNGOyZEdfwDKJQa8CXzLFPqR5&sender_id=FSTSMS&message=Peanut jar is going to be empty soon.Please get them.&language=english&route=p&numbers=9704207699')

        print(r.status_code)
    if(jar3<50):
        r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=RcIXU7uQ3HSYPhaeWLf0JkoGmbsF6w2rl9KAMtDqg5xTz48dBpn0kS7eNGOyZEdfwDKJQa8CXzLFPqR5&sender_id=FSTSMS&message=Millets jar is going to be empty soon.Please get them.&language=english&route=p&numbers=9704207699')
        
        print(r.status_code)
    if(cylinderweight<4):
        r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=RcIXU7uQ3HSYPhaeWLf0JkoGmbsF6w2rl9KAMtDqg5xTz48dBpn0kS7eNGOyZEdfwDKJQa8CXzLFPqR5&sender_id=FSTSMS&message=The Cylinder is going to be empty.Please book it soon.&language=english&route=p&numbers=9704207699')
      
        print(r.status_code)
    if(gasleak>0):
        r = requests.get('https://www.fast2sms.com/dev/bulk?authorization=RcIXU7uQ3HSYPhaeWLf0JkoGmbsF6w2rl9KAMtDqg5xTz48dBpn0kS7eNGOyZEdfwDKJQa8CXzLFPqR5&sender_id=FSTSMS&message=There is gas leak in the house and the exhaust fans turned on.&language=english&route=p&numbers=9704207699')

        print(r.status_code)
    if not success:
        print("Not connected to IoTF")
    time.sleep(2)

    deviceCli.mycommandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
