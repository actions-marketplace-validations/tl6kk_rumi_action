FROM python:3.7

WORKDIR /rumi

COPY requirements/requirements.txt .

RUN pip install -r requirements/requirements.txt

COPY rumi/ ./rumi/

COPY action.py .

CMD ["python", "action.py"]