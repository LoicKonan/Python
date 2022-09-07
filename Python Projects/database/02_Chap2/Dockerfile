FROM python:3.7.3-alpine3.9
RUN pip install fastapi uvicorn
RUN pip install psycopg2
COPY ./02_CHAP2 /02_CHAP2
WORKDIR /02_CHAP2
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "true"]
