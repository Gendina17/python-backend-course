#FROM python:3.9-alpine
#
#RUN mkdir /app
#ADD . /app/
#
#WORKDIR /app/
#
#RUN pip install -r /app/requirements.txt
#
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM ubuntu:20.04
RUN mkdir /app
ADD . /app/
RUN apt-get update
RUN apt-get install -y python3.6 python3-pip
RUN apt-get install -y python3-dev
RUN apt-get install -y postgresql-12
RUN pip3 install -r /app/requirements.txt
EXPOSE 8000
WORKDIR /app
CMD ["python3", "manage.py","runserver", "0.0.0.0:8000"]