# Use the official Python image from the DockerHub
FROM continuumio/miniconda3:main
ENV PYTHONUNBUFFERED = 1
WORKDIR /workdir
COPY requirements.txt requirements.txt
RUN yes | conda install -c conda-forge ta-lib
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /workdir
EXPOSE 8000

# Specify the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
