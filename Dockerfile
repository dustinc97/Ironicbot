FROM python:3.6-alpine

COPY . /IronicBot
WORKDIR /IronicBot

RUN apt-get update && apt-get install -y git
RUN git --version
RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME Ironic_Bot

CMD ["python", "./Bot_Main.py"]
