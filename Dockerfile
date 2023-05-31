FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3 python3-pip iproute2 net-tools

RUN echo "postfix postfix/mailname string your.hostname.com" | debconf-set-selections && \
    echo "postfix postfix/main_mailer_type string 'Internet Site'" | debconf-set-selections && \
    apt-get update && apt-get install -y postfix && \
    service postfix start

WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD service postfix start && /bin/bash
