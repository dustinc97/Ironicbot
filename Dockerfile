FROM python:3.7.1

WORKDIR /IronicBot-Release

COPY . /IronicBot-Release

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME Ironic_Bot

CMD ["python", "./Bot_Main.py"]
