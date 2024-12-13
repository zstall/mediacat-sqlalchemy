FROM python:3.12.6
# look into running apline version of python
WORKDIR /mediacatapp
COPY . /mediacatapp
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y mediainfo
RUN apt-get install -y postgresql-client
RUN apt-get clean
EXPOSE 5000
CMD flask --app main run -h 0.0.0.0 -p 5000

# look into sqlalchemy to replace pyschopg