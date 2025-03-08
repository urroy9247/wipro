text = "rahul roy"
encoded = text.encode('utf-8')

with open("binary_file2.bin","wb") as file:
    file.write(encoded)