#grep ' /api/catalog' practo.access.log
pattern =" /api/catalog"
f1 = open("file_name")
f2=""
for line in f1:
	#print line
	if pattern in line:
		f2=f2+line

#grep -v '^10\.'
f3=""
lineiterator=iter(f2.splitlines())
for line in lineiterator:
	#print line
	if ((line.find("10",0,2))== -1):
		f3=f3+line+"\n"

#cut -d' ' -f1-4 
f4=""
strip=" "
lineiterator=iter(f3.splitlines())
for line in lineiterator:
	#print line
	temp=strip.join(line.split(strip)[:4])
	f4=f4+temp+"\n"

#string to list
f5=[]
lineiterator=iter(f4.splitlines())
for line in lineiterator:
	f5.append(line)

#sort
f5.sort()


#uniq -c
f6=[]
temp=[]
for line in f5:
	if (temp.count(line)==0):
		temp.append(line)

for line in temp:
	temp2=f5.count(line)
	f6.append(str(temp2)+" "+line)

# sort -nr
f6.sort(reverse= True)

for line in f6:
	print line
















