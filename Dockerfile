#
FROM python:3.11-alpine

#
WORKDIR /code/backend
ENV PYTHONPATH=/code/backend/app
#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /code/backend/app

#
WORKDIR /code/backend/app

#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]