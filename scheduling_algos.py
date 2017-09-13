
'''
Arrival Time:       Time at which the process arrives in the ready queue.
Burst Time:         Time required by a process for CPU execution.
Completion Time:    Time at which process completes its execution.
Turn Around Time:   Time Difference between completion time and arrival time.          
     Turn Around Time = Completion Time - Arrival Time

Waiting Time(W.T): Time Difference between turn around time and burst time.
     Waiting Time = Turn Around Time - Burst Time
'''

class Process :

	pid = -1
	arrival_time = -1
	burst_time = -1
	priority = -1
	completion_time = -1
	turn_around_time = -1
	waiting_time = -1

	def __init__(self, pid, arrival_time, burst_time, priority = -1) :
		self.pid = pid
		self.arrivel_time = arrival_time
		self.burst_time = burst_time
		self.priority = priority


num_p = input('Number of processes : ')