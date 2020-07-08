import rpyc
import sys
import time
from datetime import datetime
##### Zeme #####
c = rpyc.classic.connect("localhost")

time.sleep(1)
print("Ready to message info to server")
time.sleep(1)

info = '''
from datetime import datetime
import time
def wait(n):
    start = time.time()
    time.sleep(n)
    end = time.time()
localtime = datetime.now()
print(localtime)
'''
c.execute(info)
rf = c.namespace['wait']
print(rf(10))
servertime = c.eval('localtime')
c.execute('ping = 1')
c.execute('print(ping)')
print("servertime")
time.sleep(2)

while c.eval("ping") != 2:
    time.sleep(2)
    print("waiting response")
    continue
else:
    print("Response received. 10 seconds until process execution")
    time.sleep(10)
    print("Bilde no zemes")
    print("Time:"+ datetime.now())

time.sleep(2)

moon = c.eval("moon")
print(moon)
mars = c.eval("mars")
print(mars)
