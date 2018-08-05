FROM python:3.6
ADD ./source /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD FLASK_APP=app.py FLASK_DEBUG=1 flask run