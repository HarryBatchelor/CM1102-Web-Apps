#! /usr/bin/python3
import cgi
import cgitb
import datetime
cgitb.enable()
form = cgi.FieldStorage()
form_y=form.getvalue('theYear')
y=int(form_y)
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

month = ""
if n == 3:
    month = "March"
else:
    month = "April"
st_list = (1,21,31)
nd_list = (2,22)
rd_list = (3,23)
th_list = (4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,24,25,26,27,28,29,30)
end = ""
if p in st_list:
    end = "st"
elif p in nd_list:
    end = "nd"
elif p in rd_list:
    end = "rd"
elif p in th_list:
    end = "th"

print('Content-Type: text/html; charset=utf-8')
print('')
print('<!DOCTYPE html>')
print('<html>')
print('<head><title>Finding easter</title></head>')
print('<body>')
print('<p>')
print('Easter in %s will be on %s<sup>%s</sup> %s' % (y,p,end,month))
print('</body>')
print('</html>')
