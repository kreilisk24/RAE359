import rpyc
import sys
import time
from datetime import datetime
##### Meness #####
c = rpyc.classic.connect("localhost")

time.sleep(1)
print("Connected to server")
time.sleep(1)
print("waiting request")

while c.eval("ping") != 1:
    time.sleep(5)
    print("waiting ping")
    continue
else:
    print("Request received")
    print("Sending reply")
    c.execute("ping = ping + 1")
    time.sleep(10)
    print("bilde no Meness")
    moon = '''from datetime import datetime
moon = print("Bilde no Meness"\n) + print("Time:" + datetime.now())
    '''
    c.execute(moon)
    return print("picture sent to Earth")
time.sleep(2)
