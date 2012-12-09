import sys, dircache, re, string

folder_name=sys.argv[1]
file_names=dircache.listdir(sys.argv[1])
result=[]
for i in file_names:
	#print "k"
	if(i[len(i)-4:]==".pdf"):
		print i
		result.append(i)
#print result
slide_sum=0
for i in result:
	file=open(folder_name+"/"+i,'r')
	a=file.read()	
	print i,string.count(a,"/Page")-2;
	slide_sum=slide_sum+string.count(a,"/Page")-2
	file.close()
print "Total slides to read:", slide_sum	
