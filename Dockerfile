FROM python:3.7
COPY . ./

RUN pip install -r requirements/requirements.txt
CMD ["python", "action.py"]