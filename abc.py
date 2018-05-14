import MySQLdb
import numpy as np


y = np.zeros((5,8,4) , dtype = int)
db = MySQLdb.connect("localhost","dipesh1903","12345","timedb")
cursor = db.cursor()

t_id = None 
name=None 
availability=None 
dayss = None
s_id = []
sub = []
tt_id = []
ttt_id = []
ss_id = []
deptt = []
yearr = []
aa = int(raw_input())
for i in xrange(0,aa):
	
	t_id =(int(raw_input("teacher id")))
	name = (raw_input("teacher name"))
	availability = (int(raw_input("available days")))
	dayss = (raw_input("5 bit string with 1 for available day of week and 0 for unavailable day"))
	cursor.execute("insert into teacher values(%d,'%s',%d,'%s')" % (t_id,name,availability,dayss))
	db.commit()

bb = int(raw_input("enter no. of subjects"))
for i in xrange(0,bb):
	
	s_id.append(int(raw_input("enter student id")))
	sub.append(raw_input("subject name"))

cc = int(raw_input("enter total number of teacher assigned to different subjects"))

for i in xrange(0,cc):
	
	tt_id.append(int(raw_input("teacher-subject combo id")))
	ttt_id.append(int(raw_input("teacher id")))
	ss_id.append(int(raw_input("subject id")))
	deptt.append(raw_input("department name"))
	yearr.append(int(raw_input("year")))


	

for i in xrange(0,bb):
	cursor.execute("insert into subject values(%d, '%s')" % (s_id[i], sub[i]))

for i in xrange(0,cc):
	cursor.execute("insert into teaching values(%d,%d,%d,'%s',%d)" % (tt_id[i], ttt_id[i],ss_id[i],deptt[i] , yearr[i]))


db.commit()

cursor.execute("select * from teacher ORDER BY available ASC")
rows = cursor.fetchall()
for row in rows:
	ti = row[0]
	t_name = row[1]
	available = row[2]
	days = row[3]
	cursor.execute("select dept , year , count(*) as t  from  teaching where tid = %d group by 1,2 order by t" % (ti))
	tot = cursor.fetchall()
	
	
	print(tot)
	k=0
		
	for tt in tot:
		yy= tt[1]*2 - 2
		zz = yy
		dept = tt[0]
		k=0
		
		for i in range(0,tt[2]):
			while days[k] == '1':
				if(days[k]=='1' and y[k,zz,dept]==0  ):
					y[k,zz,dept] = 1
					k += 1
					cursor.execute("select sub_name from subject where sid in (select sid from teaching where dept = %d and year = %d)" % (tt[0],tt[1]))
					s_name = cursor.fetchall()
					print("teacher %s teaches subject %s  on %d to year %d department %d" % (t_name ,s_name, k-1,tt[1],dept))
					break
					
				elif(days[k]=='1' and y[k,zz+1,dept]==0 ):
					y[k,zz,dept] = 1
					k += 1	
					cursor.execute("select sub_name from subject where sid in (select sid from teaching where dept = %d and year = %d)" % (tt[0],tt[1]))
					s_name = cursor.fetchall()
					print("teacher %s teaches subject %s  on %d to year %d department %d" % (t_name, s_name , k-1,tt[1],dept))
					break
			else:	
				k += 1
				

print(y)

db.close()




	

			
