# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError as _:
    print(f'Not file found at {fname}')
    quit()
spam_value = spam_count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    spam_confident = line.rstrip().split()[-1]
    spam_value += float(spam_confident)
    spam_count += 1

print(f"Average spam confidence: {spam_value/spam_count}")