file_location = '/home/isnakolah/Desktop/PythonFundamentals/OOP/File-Handling/text.txt'

with open('file_location', 'r') as handle:
    data = handle.read()
    print(data)