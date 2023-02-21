FROM python:3.10-slim-buster

# Inside container, new folder
WORKDIR /backend-flask

# Outside container > inside container
# this contains the libraries we want to install
COPY requirements.txt requirements.txt

# Inside container
# Install the Python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside container > inside container
#. means everything in the current directory
# first period: backend-flask(outside container)
# second period: backend-flask (inside container)
COPY . .

# Set environment variables (Env vars)
# Inside container and will remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD (command) = what will run inside the container when you run it was a container
# were running Python 3 
# -m is for module 
# 0.0.0.0 = "everything address", we need to specify this as by default it would run 
# on localhost and we don't want that fora container
# --port=4567 is a common port for Flask
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]