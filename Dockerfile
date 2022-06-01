FROM hub.hamdocker.ir/library/python:3.8

WORKDIR /src/

COPY requirements.txt .
RUN pip install -U
RUN pip install -r .requirements.txt

COPY . /scr/

EXPOSE 8000
CMD['gunicorn','University.wsgi',':8000']

