FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED 1
#RUN Django_language-website/ python manage.py runserver
WORKDIR /usr/src/lang_test
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
COPY . /usr/src/lang_test
#EXPOSE 8000
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]