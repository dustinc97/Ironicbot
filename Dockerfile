FROM gorialis/discord.py:3.6.8-alpine-rewrite-full

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./Bot_Main.py"]