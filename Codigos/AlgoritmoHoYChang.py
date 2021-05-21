import time
start=time.time()
INF = float('inf')
nINF = float('-inf')

def firstLate(schedule):
	"""
	Entrada:Trabajos agendadados en la máquina k, tal que j∈σk.
	Salida: Indice del primer trabajo que viola el plazo de entrega en la máquina k.
	"""	
	ans,i,f = None,0,0
	while ans==None and i!=len(schedule):
		if f+schedule[i][2]<=schedule[i][1]: f += schedule[i][2]
		else: ans = i
		i += 1
	return ans

def computeValues(jobs, j, ans, minSlack): return (ans[j][0], minSlack[j], jobs[j][1]-ans[j][1])
"""
Entrada:Trabajos agendadados en la máquina k, indice j del trabajo, tiempos de incio y finalización de cada trabajo y tiempo 
		mínimo de inactividad del trabajo j.
Salida: Tiempo de inicio bj, tiempo mínimo de inactividad ψj y tiempo de inactividad [ϕ(Sk)]j del trabajo j.
"""	
def checkC1(di, bj, pi): return (di>=bj+pi)
"""
Entrada:Plazo de entrega di del trabajo i∈π, tiempo de inicio bj del trabajo j∈σk y tiempo de procesamiento pi del trabajo i∈π.
Salida: Cumple o no cumple la condición.
"""	
def checkC2(minimumSlack, pi, pj): return (minimumSlack>=pi-pj)
"""
Entrada:Tiempo mínimo de inactividad ψj del trabajo j, tiempo de procesamiento pi del trabajo i∈π y tiempo de procesamiento 
		pj del trabajo j∈σk.
Salida: Cumple o no cumple la condición.
"""	
def checkC3a(slackJob, di, bj, pi): return (slackJob> di-bj-pi)
"""
Entrada:Tiempo de inactividad [ϕ(Sk)]j del trabajo j, plazo de entrega di del trabajo i∈π, tiempo de inicio bj del trabajo j∈σk 
		y tiempo de procesamiento pi del trabajo i∈π.
Salida: Cumple o no cumple la condición.
"""	
def checkC3b(di, dj, pi, pj, jobCnt, j): return [(di>dj),(pi>pj),((pi-pj)*(jobCnt-j) > (di-dj))]
"""
Entrada:Plazo de entrega di del trabajo i∈π y dj del trabajo j∈σk, tiempo de procesamiento pi del trabajo i∈π y pj del trabajo j∈σk,
		número de trabajos agendados a tiempo en la maquina k e indice j del trabajo.
Salida: Cumple o no cumple la condición.
"""	
def H2(jobs, M):

	"""
	Entrada:Colección de trabajos A[0…I) y Número de máquinas.
	Salida: Secuencia de la máxima cantidad de trabajos de A[0…I) que no violan el plazo límite de entrega en su respectiva máquina, 
			lista de rechazados y lista de imposibles.
	"""
	###Initialize
	N= len(jobs)
	schedules=[[] for _ in range(M)]
	unscheduled,rejected,impossible = [],[],[]

	"""
	Si el tiempo de procesamiento de los trabajos es mayor a su plazo de entrega, tal que pi>di estos se ubican en la lista de imposibles.
	De lo contrario, son añadidos a la lista de unscheduled. 
	"""	
	for i in range(len(jobs)):
		if(jobs[i][2]>jobs[i][1]):
			impossible.append(jobs[i])
		else:
			unscheduled.append(jobs[i])
	###Initialize
	###H2
	for k in range(M):
		"""
		Agendar en la secuencia de la máquina los trabajos pertenecientes a la lista de no agendados y organizarlos de acuerdo a su
		plazo de entrega (EDD)
		"""
		schedules[k]=unscheduled
		unscheduled =[]
		schedules[k].sort(key = lambda x: (x[1],x[2]))
		ans= firstLate(schedules[k])
		"""
		Si en la secuencia de la máquina se encuentra un trabajo Jq que viola su plazo de entrega, revisar la secuencia desde la
		posición inicial hasta el incumplimiento de la restricción J1 …Jq (ans+1), encontrar el trabajo con un tiempo de procesamiento
		mayor Jmax dentro de esta subsecuencia, removerlo de la secuencia actual y añadirlo a la lista de no agendados.
		(Continuar realizando esta acción hasta que no existan más trabajos que sobrepasen su plazo de entrega).
		"""
		while(ans != None):
			maxPi=nINF
			for i in range(ans+1):
				if(maxPi<schedules[k][i][2]):
					maxPi=schedules[k][i][2]
					jMax=schedules[k][i]
			schedules[k].remove(jMax)
			unscheduled.append(jMax)
			ans= firstLate(schedules[k])
		
		#Si la lista de no agendados no se encuentra vacía π≠Ø y aún no han sido revisadas todas las máquinas
		if((k<M-1) and (len(unscheduled)!=0)):
			ans2 = [ None for _ in schedules[k]]
			f = 0
			#Calculo de tiempo de inicio de cada trabajo j∈σk de la máquina k 
			for l in range(len(schedules[k])):
				ans2[l] = (f, f+schedules[k][l][2])
				f += schedules[k][l][2]
			#Calculo del tiempo mínimo de inactividad ψj del trabajo j (minSlack) en la máquina k como es propuesto mediante (9)
			minSlack = [ INF for _ in schedules[k]]
			for q in range(len(schedules[k])-1):
				for r in range(q+1,len(schedules[k])):
					minSlack[q]= min(minSlack[q], schedules[k][r][1]-ans2[r][1])
			"""
			Sea j=0 el primer trabajo en σk (schedules) e i=0 el primer trabajo en 𝜋 (unscheduled), se calcula el tiempo de inicio bj, 
			tiempo de inactividad [ϕ(Sk)]j y tiempo mínimo de inactividad ψj de cada trabajo j∈σk de la máquina k.
			"""
			for j in range(len(schedules[k])):
				for i in range(len(unscheduled)):
					ans=computeValues(schedules[k], j, ans2, minSlack)
					dj, pj=schedules[k][j][1], schedules[k][j][2]
					di, pi= unscheduled[i][1], unscheduled[i][2]
					bj, minimumSlack, slackJob = ans
					jobCnt=len(schedules[k])
					"""
					Se verifica el cumplimiento de las condiciones propuestas por Ho y Chang. De cumplirse con las mismas se
					intercambia el trabajo j∈σk de la máquina k por el trabajo i∈π de la lista de no agendados y se calcula 
					nuevamente el tiempo de inicio bj y tiempo mínimo de inactividad ψj de cada trabajo j∈σk de la máquina k.
					"""
					if(checkC1(di, bj, pi) and checkC2(minimumSlack, pi, pj) and (checkC3a(slackJob, di, bj, pi) or (False not in checkC3b(di, dj, pi, pj, jobCnt, j)))):
						aux = schedules[k][j]
						schedules[k][j]= unscheduled[i] ##Swap
						unscheduled[i]= aux
						if(j==0):
							f=0
						else:
							f=ans2[j-1][1]
						for l in range(j, len(schedules[k])):
							ans2[l] = (f, f+schedules[k][l][2])
							f += schedules[k][l][2]
						for q in range(len(schedules[k])-1):
							for r in range(q+1,len(schedules[k])):
								minSlack[q]= min(minSlack[q], schedules[k][r][1]-ans2[r][1])
						#print("Hubo un swap de:", schedules[k][j], unscheduled[i])
						#print("-------------------------------------------")
	rejectedJobs=unscheduled
	print("Execution time", time.time()-start)
	#Impresión de resultados
	for i in schedules:
		for j in i:
			print(j[0])
		print()
	t=0
	for i in range(len(schedules)):
		for j in range(len(schedules[i])):
			t+=1
	print(t)				
	###H2
	return [schedules, rejected, impossible]
def main():
	"""
	Entrada:Colección de trabajos A[0…I), I≥0 tal que A[i] contiene la tupla (Ji,di,pi) indicando el nombre, plazo máximo 
			de entrega y tiempo de procesamiento del trabajo i, 0≤i≤I, respectivamente; Número de máquinas M.
	Salida:Secuencia de la máxima cantidad de trabajos de A[0…I) a ser procesados en cada máquina que no violan el 
			plazo límite de entrega; Trabajos rechazados e imposibles.
	"""
	M=2
	jobs=[]
	n=50
	for i in range(n+1):
		if (i==0):
			nada=input()
		else:
			Ji,di,pi=input().strip().split(";")
			jobs.append([Ji,float(di),float(pi)])
	schedules, rejected, impossible = H2(jobs, M)
main()
