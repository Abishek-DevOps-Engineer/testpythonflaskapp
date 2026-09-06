FROM python:3.13.13-alpine3.23

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python3" , "app.py"]