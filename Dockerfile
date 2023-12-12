FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./wait-for-it.sh /code/wait-for-it.sh

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["./wait-for-it.sh" , "elasticsearch:9200" , "--strict" , "--timeout=300" , "--" ,"uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]
