import random
def main():
	print("JOB,Deadline,PT")
	n=10
	q=5
	m=2
	jobs=[]
	days = [1, 2, 3, 4, 7, 8, 9, 10, 11]
	for i in range(n):
		jobs.append([i+1, None, None])
	tMean=0
	i=0
	while(i<n):
		ti=random.gammavariate(1.444, 2.2)
		if(ti>=1 and ti<=20):
			jobs[i][2]= ti
			tMean+=ti
			i+=1
	tMean=tMean/n
	for i in range(n):
		di=(random.choice(days)*24)+9
		jobs[i][1]=di
	for i in jobs:
		print(str(i[0])+";"+str(i[1])+";"+str(i[2]))
main()