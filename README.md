# Minimizar el número de trabajos tardíos en máquinas paralelas sujeto a restricciones de disponibilidad
## Descripción
 Dada la creciente necesidad de satisfacer al usuario por encima de crear un cronograma de trabajo que reduzca el costo de fabricación/operación en talleres donde la maquinaria o equipos consumen un gasto eléctrico constante al no poder ser desconectados y el proceso se encuentra sujeto a la disponibilidad del operario para iniciar el desarrollo de una actividad, a continuación se propone un modelo de programació lineal para la disminución del número de trabajos tardíos en máquinas paralelas atendiendo a restricciones de disponibilidad de un taller de trabajo, cuando las actividades son planeadas en un instante cero y la última por ser ejecutada durante la jornada de trabajo puede continuar siendo procesada durante el periodo de no disponibilidad en cada máquina hasta que sea terminada (sin sobrepasar la nueva jornada de trabajo). Además, se presenta la implementación del algoritmo desarrollado por Moore y Hodgson para garantizar optimalidad en el agendamiento del menor número de trabajos tardíos en una sola máquina; el modelo propuesto por Süer, Báez y Z. Czajkiewicz, así como la heurística desempeñada por Ho y Chang para extender el problema a un conjunto de máquinas paralelas idénticas y el modelo planteado por Almasarwah, Chen, Süer y Yuan para asignar restricciones de disponibilidad al agendamiento. 
## Prerrequisitos
 Para los modelos en formato .pynb se posee como prerrequisito descargar Anaconda y Gurobi (remitirse al manual de instalación adjuntado en pdf).
## Pasos para ejecutar el código
1.	Crear un archivo .csv que posea el siguiente formato:
|JOB|Deadline|PT|
|----------:|-----------:|----------:|
|          1|	          4|          2|
|          2|	          2|          1|
|          3|	          1|          1|

Donde la primera columna posee el indicativo de la solicitud, la segunda su plazo de entrega y la tercera su tiempo de procesamiento.
### Para ejecutar los archivos .pynb, es decir, el Modelo de Süer et. al, Almasarwah et. al, y el propuesto por mí:
2.	Presionar “Run” al código del Notebook de Jupyter.
3.	Ingresar el nombre del archivo acompañado de su formato (.csv). e.g. “solicitudes.csv”
### Para ejecutar los archivos .py, es decir, el algoritmo propuesto por Moore y la heurística de Ho y Chang:
2. Cambiar el n del código en función del número de trabajos que desee procesar 
3. Abrir una ventana de Símbolo del Sistema
4. Ingrese a la carpeta donde posee guardado el código y el archivo con las solicitudes que desea agendar.
5. Ingrese el nombre del archivo que posee las solicitudes seguido del nombre del código. e.g. “python AlgoritmoHoYChang.py < solicitudes.csv” o “python AlgoritmoMoore.py < solicitudes.csv”
#### Recuerde no incluir las comillas cuando ingrese algún nombre de archivo. Por otro lado, tome en cuenta que el código esta implementado para realizar el agendamiento en dos máquinas paralelas, por tanto, si desea agendar más cambie el parámetro M=2 (salvo en el algoritmo de moore donde únicamente las solicitudes pueden ser secuenciadas en una máquina).
