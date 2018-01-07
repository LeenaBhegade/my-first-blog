FROM python:3.5-alphine
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD entrypoint.sh /code/
RUN chmod +x entrypoint.sh