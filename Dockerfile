FROM python:3.6

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/
RUN python manage.py collectstatic --no-input

CMD python manage.py runserver_plus 0.0.0.0:8000