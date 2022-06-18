FROM python:3.9

WORKDIR /telegrambot

ADD . /telegrambot/

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]