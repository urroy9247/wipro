# Use the official image as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY docpysc1.py . /app

#install flask
#RUN pip install flask

#Expose Flask Port
#EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "docpysc1.py"]

