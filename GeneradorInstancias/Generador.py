import random
def main():
	print("JOB;Deadline;PT")
	n=150
	q=3.5
	m=4
	jobs=[]
	for i in range(n):
		jobs.append([i+1, None, None])
	tMean=0
	for i in range(n):
		ti=random.uniform(1, 20)
		jobs[i][2]= ti
		tMean+=ti
	tMean=tMean/n
	for i in range(n):
		di=random.uniform(1, (2*n*tMean)/(q*m))
		jobs[i][1]=di

	jobs.sort(key = lambda x: (x[1],x[2]))
	for i in jobs:
		print(str(i[0])+";"+str(i[1])+";"+str(i[2]))
main()