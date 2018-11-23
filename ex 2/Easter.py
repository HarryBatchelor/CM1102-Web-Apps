#!/usr/bin/python3
import cgi, cgitb
form = cgi.FieldStorage()
import datetime
y = form.getvalue(year)
print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head><title> finding easter python script</title></head>')
print('<body>')
print('<p>')
print('''
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    print(datetime.date(day=p,month=n,year=y)) ''')
print('<p>')
print('</body>')
print('</html')
