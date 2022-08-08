# Minimize the number of tardy jobs on *m* identical parallel machines based on availability constraints
## Description
 In this project, a linear programming model is presented to reduce the number of tardy jobs in a workshop in which the machinery must remain connected, and the execution of activities is subject to the availability intervals of the establishment. The proposed model considers the case in which the last activity scheduled during the working day in each machine can continue processing during the unavailability period until finished, avoiding exceeding the new working day.
 As part of the study, also is presented the implementation of the algorithm developed by Moore and Hodgson to schedule the least number of late jobs on a single machine; the model proposed by Süer, Báez, and Z. Czajkiewicz, as well as the heuristics performed by Ho and Chang to extend the problem to a set of identical parallel machines and the model proposed by Almasarwah, Chen, Süer and Yuan to assign availability constraints to the scheduling.
## Prerequisites
 For models in .ipynb format, it is a prerequisite to download Anaconda and Gurobi (refer to the installation manual in pdf).
## Steps to run the code
1.	Create a .csv file that has the following format:

|JOB|Deadline|PT|
|----------:|-----------:|----------:|
|          1|	          4|          2|
|          2|	          2|          1|
|          3|	          1|          1|

The first column is the indicative of the request, the second its delivery time and the third its processing time.
### To run the .ipynb files, i.e., the Model of Süer et al., Almasarwah et al., and the one proposed by me:
2.	Press "Run" to the Jupyter Notebook code.
3.	Enter the file name along with its format (.csv). e.g. “requests.csv”
### To run the .py files, i.e. the algorithm proposed by Moore and the Ho and Chang heuristics:
2. Change the n parameter of the code based on the number of jobs you want to process
3. Open a Command Prompt window
4. Enter the folder where you have saved the code and the file with the requests you want to schedule.
5. Enter the file name followed by the code name. e.g. “python AlgoritmoHoYChang.py < requests.csv” or “python AlgoritmoMoore.py < requests.csv”
#### Remember not to include quotation marks ("") when entering any file names. On the other hand, take into account that the code is implemented to perform the scheduling on two parallel machines, therefore, if you want to schedule more, change the parameter M=2 (except in Moore's algorithm where only the requests can be sequenced in one machine).
