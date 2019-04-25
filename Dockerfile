FROM ubuntu:18.10

RUN apt-get update
RUN apt-get install -y python3-pip nginx default-libmysqlclient-dev
RUN pip3 install django boto3 gunicorn

ADD . /home/ubuntu/pseudotest

WORKDIR /home/ubuntu/pseudotest


RUN ./scripts/install_dependencies.sh

RUN echo "#!/bin/bash" > scripts/docker_start.sh &&\
    echo "sleep 15" >> scripts/docker_start.sh &&\
    echo "./scripts/migrate.sh" >> scripts/docker_start.sh &&\
    echo "./scripts/start_application.sh" >> scripts/docker_start.sh &&\
    chmod +x scripts/docker_start.sh

CMD [ "./scripts/docker_start.sh" ] 

