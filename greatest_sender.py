# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
# appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop
# to find the most prolific committer.

# first solution

name = input("Enter file:")
if len(name) < 1:
    name = "files/mbox-short.txt"
handle = open(name)

word_counts = {}
for line in handle:
    if 'From ' not in line:
        continue
    sender = line.split()[1]
    word_counts[sender] = word_counts.get(sender, 0) + 1

# Solution 1
biggest = ''
counts = 0
for key, value in word_counts.items():
    if value > counts:
        biggest = key
        counts = value

print(biggest, counts)

# Solution 2
reverse_sorted_list = sorted([(v, k) for k, v in word_counts.items()], reverse=True)
print(reverse_sorted_list[0][1], reverse_sorted_list[0][0])

