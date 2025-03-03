FROM python:3.9-alpine

WORKDIR /app

COPY scripts.py .
COPY IF-1.txt /home/data/
COPY AlwaysRememberUsThisWay-1.txt /home/data/

RUN mkdir -p /home/data/output

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

CMD ["python", "scripts.py"]
