FROM arm64v8/python:3.12.8




WORKDIR /


COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
