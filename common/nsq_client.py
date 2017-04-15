
import requests
import threading
import json
from datetime import datetime



def send_to_nsq(topic, message):
    if not isinstance(message, str):
        return {'code': -1, 'reason': 'the message must be string'}
    if not isinstance(topic, str):
        return {'code': -1, 'reason': 'the topic must be string'}
    url = "http://127.0.0.1:4151/put?topic=" + topic
    r = requests.post(url, data=message) 
    print r.text
    if r.text == 'OK':
        return {'code': 0, 'msg': 'success'}
    else:
        return {'code': -1, 'reason': r.text}

class NsqThread(threading.Thread):
    
    def __init__(self, name='xixi'):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print self.name + ":" + str(datetime.now())
        send_to_nsq('test_topic', json.dumps({'name':self.name}))

if __name__ == '__main__':
    res = []
    for i in range(0, 100):
        res.append(NsqThread(name=str(i)+'th player'))
    for x in res:
        x.start()
