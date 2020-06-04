file_location = '/home/isnakolah/Desktop/PythonFundamentals/OOP/File-Handling/text.txt'

handle = open(file_location, 'r')

data = handle.read()
counter = 0

for word in data.split():
    if word == 'Python':
        counter += 1

print(counter)