#Project Euler Problem 19
#Solution : Brandon Greer
import datetime

start_date = datetime.date(1901,1,1).toordinal()
end_date = datetime.date(2001,1,1).toordinal()

sunday_count = 0

#this one was pretty hevily influenced by stack overflow
#I thought I was looking at a sloution to a slightly 
#different problem (the asker gave a different date range
# and I tottally missed the requiremnt that the sunday fall
# on the 1st of the month on my first read through)

for date in range(start_date, end_date):
    date = datetime.date.fromordinal(date)
    if(date.weekday() == 6 and date.day == 1):
        sunday_count += 1

print(sunday_count)