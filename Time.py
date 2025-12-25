#6 . time obj

import datetime as dt
time1=dt.time(11, 20,30,2000) #micro seconds Will not Showing excced M & S !
print(time1)


#7.
import datetime as dt
time1=dt.time(11, 20,30,2000)
print("hour" , time1.hour)
#print("M" , time.M)
#print("S" , time.S)
#print("MS" , time.MS)


#8.
import datetime as dt
CT =dt.datetime.now()
#print(CT)
print(CT.hour)
#Print(CT.minute)
#Print(CT.second)
#Print(CT.microsecond)


#9
#import datetime as dt
#CDT=dt.datetime.now()
#PD=dt.datetime(1,1,2000)
#rem_D=(CDT-PD)
#print("The diff is :- ".rem_D)

one_week = dt.timedelta(days=7)
next_week =  CT + one_week
print("next_week :- ", next_week)

one_week = dt.timedelta(days=7)
past_date =  CT - one_week
print("past_date :- ", past_date)


print(help(dt))



