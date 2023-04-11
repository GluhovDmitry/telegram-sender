FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

RUN python setup.py develop
ENTRYPOINT ["tg_api"]
EXPOSE 8080/tcp