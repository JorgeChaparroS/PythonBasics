from datetime import date, datetime

d = date.today()
dx = datetime.now()
print(d)

d1 = d.strftime("%d/%m/%y")
print(d1)

d2 = d.strftime("%A %d/%m/%y")
print(d2)

d3 = dx.strftime("%A %d/%m/%Y %H:%M:%S")
print(d3)

d4 = dx.strftime("%A %I:%M:%S%p %d/%m/%Y")
print(d4)

d5 = dx.strftime("%A %d %B %Y %I:%M:%S%p")
print(d5)