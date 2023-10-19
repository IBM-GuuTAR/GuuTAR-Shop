From python:3.9-slim

WORKDIR /backend

RUN apt-get update && apt-get install git -y

RUN pip3 install pipenv

COPY . /backend

RUN pipenv requirements > requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "main.py"]

