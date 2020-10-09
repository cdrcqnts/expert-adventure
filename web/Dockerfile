FROM python:latest
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# CMD ["python", "app.py"]
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]