import operator

class processes :

	pid = 0;
	arrival_time = 0;
	burst_time = 0;
	priority = 0;

	def __init__ (self, processID, arrival, bursted, pri) :
		self.pid = processID
		self.arrival_time = arrival
		self.burst_time = bursted
		self.priority = pri

	def print_this (self) :
		print ( self.pid, self.arrival_time, self.burst_time, self.priority)



n_pids =  input ( " Number of process IDs : ")
print('')
process_list = []

#Inputs
for _ in range(n_pids):

	pid = input ( " PID : " )
	arrival_time = input ( " Arrival Time : " )
	burst_time = input ( " Burst Time : " )
	priority = input ( " Priority : " )

	p = processes(pid,arrival_time,burst_time,priority)

	process_list.append(p)

	print('')

	
# First Come First Server
print ( "FIRST COME FIRST SERVE :\n" )
print ('|'),

process_list.sort ( key = operator.attrgetter('arrival_time') )

for x in range(len(process_list)):
	for _ in range(process_list[x].burst_time):
		print "P",process_list[x].pid,"|",


# Non- primtive Shortest time 
print ("\n\n NON-PRIMTIVE SHORTEST JOB :\n"  )
print ('|'),


process_list.sort ( key = operator.attrgetter('burst_time'))

for x in range(len(process_list)):
	for _ in range(process_list[x].burst_time):
		print "P",process_list[x].pid,"|",

#for x in range(len(process_list)) :
#	process_list[x].print_this()

#Primtive Shortest time
print ("\n\n PRIMTIVE SHORTEST JOB :\n"  )
print ('|'),

process_list.sort (key = operator.attrgetter('arrival_time'))
max_arrival_time = max(p.arrival_time for p in process_list)

s_list = []

for i in range(max_arrival_time + 1):

	for p in process_list :
		if p.arrival_time == i :
			s_list.append(p)

	s_list.sort (key = operator.attrgetter('burst_time'))
	print "P",s_list[0].pid,"|",
	s_list[0].burst_time -= 1
	if s_list[0].burst_time == 0 :
		s_list.pop(0)

while len(s_list) != 0:
	s_list.sort (key = operator.attrgetter('burst_time'))
	print "P",s_list[0].pid,"|",
	s_list[0].burst_time -= 1
	if s_list[0].burst_time == 0 :
		s_list.pop(0)


#ROUND ROBIN
