FROM python:3.6
RUN apt-get update
COPY . /webapp
RUN pip install --no-cache-dir -r /webapp/app/requirements.txt
ENV FLASK_ENV="docker"

WORKDIR /webapp/app

EXPOSE 5000

CMD [ "python", "/webapp/app/app.py" ]

