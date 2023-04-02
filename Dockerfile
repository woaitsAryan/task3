FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api.py .

COPY script.sh .

RUN chmod +x script.sh

COPY project.py .

CMD ["./script.sh"]
