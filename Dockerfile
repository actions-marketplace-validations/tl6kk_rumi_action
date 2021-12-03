FROM python:3.7

WORKDIR /rumi

COPY . .

RUN pip install -r requirements/requirements.txt

CMD ["python", "/rumi/action.py"]