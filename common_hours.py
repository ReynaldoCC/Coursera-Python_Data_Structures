# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
# messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
# time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "files/mbox-short.txt"
handle = open(name)
hours_rate = {}
for line in handle:
    if not line.startswith('From '):
        continue
    time_sent = line.rstrip().split()[-2]
    hour = time_sent.split(':')[0]
    hours_rate[hour] = hours_rate.get(hour, 0) + 1

for k, v in sorted(hours_rate.items()):
    print(k, v)
