# Modulo and time difference
# In arithmetic, the remainder (or modulus) is the amount "left over" after performing the division
# of two integers which do not divide evenly (from Wiki). This task will provide further practice
# with modulo operation.  Suppose, we are given two timestamps - for example, when the train or ferry
# boat starts its travel and when it finishes. This may look like:
#  start: May 3, 17:08:30
#  end  : May 8, 12:54:15
# and we are curious to know, how much time (in days, hours, minutes and seconds) is spent in traveling
# (perhaps, to choose faster variant). How this could be achieved?
# One of the easiest way is:
# * convert both timestamps to big numbers, representing seconds from the beginning of the month (or year,
#   or century);
# * calculate their difference - i.e. travel time in seconds;
# * convert this difference back to days, hours, minutes and seconds.
# First operation could be performed by multiplying minutes by 60 and hours by 60*60 etc. and summing all
# values up. The third operation should be performed on contrary by several divisions with keeping remainders.
# In this task we are given several pair of timestamps. We suppose that both dates in the pair are always
# in the same month, so only number of day will be given. We want to calculate difference between timestamps
# in each pair.
# Input data: the first line contains number of test-cases, other lines contain test-cases themselves. Each
# test-case contains 8 numbers, 4 for each timestamp: day1 hour1 min1 sec1 day2 hour2 min2 sec2 (second
# timestamp will always be later than first).
# Answer: for each test-case you are to output difference as following (days hours minutes seconds) -
# please note brackets - separated by spaces.
#  input data:
#   3
#   1 0 0 0 2 3 4 5
#   5 3 23 22 24 4 20 45
#   8 4 6 47 9 11 51 13
#  answer:  (1 3 4 5) (19 0 57 23) (1 7 44 26)

numbers = '25 20 49 41 27 20 16 51 3 2 20 53 14 8 9 20 18 1 20 29 19 8 41 8 20 23 33 45 27 11 54 54 1 18 37 3 27 17 16 15 22 23 43 56 26 1 20 9 3 19 46 41 6 5 49 19 14 16 25 15 24 21 21 50 16 21 48 15 29 12 59 37 1 22 9 9 18 3 35 52 26 3 32 8 27 0 25 6 3 22 57 51 18 19 44 11'
num_list = numbers.split()
values = []
days = (24*60**2)
hours = (60**2)
minutes = (60)
seconds = 1
difference = []
line = 0
syad = 0
dremainder = 0
sruoh = 0
hremainder = 0
setunim = 0

for num in num_list:
    values.append(int(num))

for i in range(0,len(values),8):
    difference.append((values[i]) * days)
    difference.append((values[i+1]) * hours)
    difference.append((values[i+2]) * minutes)
    difference.append(values[i+3])
    difference.append((values[i+4]) * days)
    difference.append((values[i+5]) * hours)
    difference.append((values[i+6]) * minutes)
    difference.append(values[i+7])
    line = sum(difference[i+4:i+8]) - sum(difference[i:i+4])
    syad = round(int(line / days))
    dremainder = line % days
    sruoh = round(int(dremainder / hours))
    hremainder = dremainder % hours
    setunim = round(int(hremainder / minutes))
    seconds = hremainder % minutes
    print(f'({syad} {sruoh} {setunim} {seconds})', end=' ')