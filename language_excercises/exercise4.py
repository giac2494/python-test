import sys

def reads(words):
    html = ""
    tmp = 0
    for word in words:
        if(tmp != 0):
            html += '<p>'+word+'</p>\n'
        tmp = 1
    return html

print reads(sys.argv)