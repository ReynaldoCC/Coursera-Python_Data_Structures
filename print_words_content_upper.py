# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except FileNotFoundError as _:
    print(f'File not exists at {fname}')
    quit()
file_content = fh.read()
print(file_content.upper().rstrip())
