FROM python:3.7
COPY rumi rumi
COPY requirements/requirements.txt requirements/requirements.txt

RUN pip install -r requirements/requirements.txt
CMD ["python", "action.py"]