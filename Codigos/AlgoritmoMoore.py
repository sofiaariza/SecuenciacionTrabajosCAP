def algoritmoMoore():
	jobs= list()
	n=50
	for i in range(n+1):
		if (i==0):
			nada=input()
		else:
			Ji,di,pi=input().strip().split(";")
			jobs.append((Ji,float(di),float(pi)))

	"""
	Entrada: Colección de trabajos A[0…I), I≥0 tal que A[i] contiene la lista [Ji,di,pi] indicando el nombre, plazo máximo de entrega
			y tiempo de procesamiento del trabajo i, 0≤i≤I, respectivamente.
	Salida: Secuencia de la mínima cantidad de trabajos en A[0…I) que no violan el plazo límite de entrega.
	"""
	accepted,rejected,impossible,unscheduled,ans,f = [],[],[],[],[],0
	"""
	Los trabajos son ordenados de acuerdo con la regla EDD (Plazo de entrega más temprano), tal que d0≤…di…≤dI, J0≤…Ji…≤JI y su 
	sencuencia es reconocida como la actual (unscheduled).
	"""
	unscheduled=jobs.copy()
	unscheduled.sort(key = lambda x: (x[1],x[2]))
	"""
	Son eliminados de la secuencia aquellos trabajos imposibles de realizar, es decir aquellos con un plazo de entrega por debajo 
	de su tiempo de procesamiento.
	"""	
	for l in range(len(jobs)):
		if(jobs[l][2]>jobs[l][1]):
			impossible.append(jobs[l])
			unscheduled.remove(jobs[l])

	for i in range(len(unscheduled)):
		di,ti= unscheduled[i][1],unscheduled[i][2]
		if(f+ti<=di):
			"""
			Si el tiempo de finalización del trabajo anterior junto al de procesamiento del nuevo no sobrepasan su plazo de entrega,
			añadir el trabajo a la lista de aceptados.
			"""
			accepted.append(unscheduled[i])
			f+=ti
		else:
			"""
			De lo contrario, revisar la secuencia desde la posición inicial hasta el incumplimiento de la restricción J1…Jq, 
			encontrar el trabajo con un tiempo de procesamiento mayor Jmax dentro de esta subsecuencia, y añadirlo a la lista de 
			rechazados. 
			"""
			jMax=max(accepted+[unscheduled[i]], key = lambda x: x[2])
			if(jMax in accepted):
				accepted.remove(jMax)
				accepted.append(unscheduled[i])
				f+=ti-jMax[2]
			rejected.append(jMax)
	
	f=0
	for i in range(len(accepted)):
		ans.append([accepted[i][0], f, f+accepted[i][2]])
		f+=accepted[i][2]
	
	print("La trabajos que no serán entregados a tiempo son:", len(rejected))
	print("La trabajos imposibles de realizar son:", len(impossible))
	print("La secuencia a desempeñar para entregar los trabajos a tiempo es la siguiente:")

	for i in ans:
		print(i)
	return ans
algoritmoMoore()