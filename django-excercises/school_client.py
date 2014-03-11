import requests
import json
import argparse

HOST = 'localhost:8000'

def enroll_student(f_name, l_name):
    resp =requests.post(
        'http://{}/home'.format(HOST),
        json.dumps({'f_name':f_name,'l_name':l_name}))
    if resp.status_code == 200:
        print 'OK'
    else:
        print 'Errore'

def search_student(student):
    resp = requests.get('http://{}/home'.format(HOST))
    content = json.loads(resp.content)
    for stud in content:
        if(stud['f_name'] == student or stud['l_name']== student):
            print stud['f_name'] + " " + stud['l_name']+ " "+ stud['time']

parser = argparse.ArgumentParser('student client')
parser.add_argument('command')
parser.add_argument('--f_name')
parser.add_argument('--l_name')
parser.add_argument('--student')
args = parser.parse_args()

if args.command == 'enroll':
    enroll_student(args.f_name, args.l_name)
elif args.command == 'search':
    search_student(args.student)
else:
    print 'Errore'