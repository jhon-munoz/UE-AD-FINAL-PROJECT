FROM python:3.10.5
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app/
CMD ["uvicorn", "server:store", "--host", "0.0.0.0", "--port", "80"]
