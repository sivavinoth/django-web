FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV DEBUG=1
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:80000"]
