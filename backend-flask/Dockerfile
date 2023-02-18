FROM python:3.10-slim-buster

# Inside container, new folder
WORKDIR /backend-flask

# Outside container > insdie container
COPY requirements.txt requirements.txt

# Inside container
# Install the python libraries used for the app
RUN pip3 install -r requirements.txt

# Outside container > inside container
#. means everything in the current directory
# first period: backend-flask(outside container)
# second period: backend-flask (inside container)
COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD (command)
# python3 -m flask run --host=0.0.0.0 --port=4567
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]