FROM python:3.9.10-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD python app.py