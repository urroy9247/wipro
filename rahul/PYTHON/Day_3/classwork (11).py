with open('photo1.jpg', 'rb') as f1:  # Read the image as binary

    img_data = f1.read()
 
with open('doss.jpg', 'wb') as f2:  # Write binary data

    f2.write(img_data)
 
print("Image copied successfully.")

 