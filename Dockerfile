FROM python:3.6-slim

CMD ["./update_slack_status.py"]
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./update_slack_status.py .
