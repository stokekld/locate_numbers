FROM python:3

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip3 install -r requirements.txt

EXPOSE 9000

CMD ["python", "api.py"]