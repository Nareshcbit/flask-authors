FROM python:3.6
RUN apt-get update
COPY . /webapp
RUN sudo apt-get install python3-pip
RUN sudo pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /webapp/app/requirements.txt
ENV FLASK_ENV="docker"

WORKDIR /webapp/app

EXPOSE 5000

CMD [ "python", "/webapp/app/app.py" ]

