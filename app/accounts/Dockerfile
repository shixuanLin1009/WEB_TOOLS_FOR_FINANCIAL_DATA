# Use the official Python image from the DockerHub
FROM continuumio/miniconda3:main
ENV PYTHONUNBUFFERED = 2
WORKDIR /workdir
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN yes | pip install psycopg2-binary

# Copy the current directory contents into the container at /app
COPY . /workdir
EXPOSE 8001

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
