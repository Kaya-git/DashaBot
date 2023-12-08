FROM python:3.11.6

ENV BOT_TOKEN=6428826459:AAEVOR31vZh8LOlHcdUrK3SZS1Kr_ogljEU

RUN mkdir /dasha_bot

WORKDIR /dasha_bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src

CMD python3.11 main.py