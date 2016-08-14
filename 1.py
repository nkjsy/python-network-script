import re
fhand=open("regex_sum_301733.txt")
sm=0
for line in fhand:
    nlist=re.findall('[0-9]+',line)
    for n in nlist:
        sm=sm+int(n)
print (sm)