FROM python:3.12-alpine

# set a working directory inside the container
WORKDIR /app

# copy and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the source code of app
COPY app.py .

# expose flask port
EXPOSE 5000

CMD ["python", "app.py"]