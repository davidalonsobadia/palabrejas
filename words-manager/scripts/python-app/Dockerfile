FROM python:3

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

# install psycopg2 library with PIP
COPY requirements.txt /
COPY add_data_in_db.py /

RUN pip3 install -r requirements.txt

CMD ["python3", "add_data_in_db.py"]

