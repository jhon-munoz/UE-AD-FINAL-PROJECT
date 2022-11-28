FROM python:3.10.5
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app/
ENV token eyJhbGciOiJIUzI1NiJ9.bWF0Y2hlcw.ux15vZfKAOgACBxdSry1w62KQfpj2cI3djOUPU2k7ek
CMD ["uvicorn", "server:matches", "--host", "0.0.0.0", "--port", "80"]
