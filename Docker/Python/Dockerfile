# Get python as a base image
FROM python:3
# Create a directory
RUN mkdir /usr/src/app
# Set the directory as the work directory
WORKDIR /usr/src/app
# Copy everything in the current directory over to the new directory
COPY . .
# Run main.py
CMD [ "python", "main.py" ]