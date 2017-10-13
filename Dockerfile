# Use Python3 base image
FROM python:3

# Copy our dependency file to this container
# ADD requirements.txt /requirements.txt

# Make a code directory
RUN mkdir /code/

# Change directory to code/
WORKDIR /code/

# Add all project files to code directory in our image
ADD requirements.txt /code/

# Install specified packages
RUN pip3 install -r requirements.txt

ADD . /code/

# Allow container to listen on port 8000
EXPOSE 8000

# Build and run django project
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
# CMD ["python3", "manage.py", "runserver"]
RUN python3 manage.py runserver 0.0.0.0:8000
