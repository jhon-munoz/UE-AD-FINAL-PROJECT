FROM python:3.10.5
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app/
ENV token eyJhbGciOiJIUzI1NiJ9.c3RvcmU.RHcoS_9UexhdnUcZsDq-UgdmeWqHmFY5IuqcTy4OVY4
CMD ["uvicorn", "server:store", "--host", "0.0.0.0", "--port", "80"]
