FROM gorialis/discord.py:3.6-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV NAME Ironic_Bot

COPY . .

CMD ["python", "./Bot_Main.py"]
