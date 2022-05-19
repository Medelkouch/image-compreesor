FROM python:3.9

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apt update && apt install nano

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code

# RUN chmod -R 777 /app/logs
# RUN chmod -R 777 /app/storage


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ,"--reload"]



