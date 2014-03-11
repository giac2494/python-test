import json
import requests

response = requests.get('http://ialpython.apiary.io/laboratories')
lab = json.loads(r.content)

print 'Network Down:'

for la in lab:
	if la['network_status'] == 'down':
		print la['name']

print '\n'