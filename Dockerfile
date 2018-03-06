FROM registry.centos.org/centos/centos:latest

RUN yum -y update &&\
    yum -y install python-flask &&\
    yum clean all

ADD app.py /
RUN chmod a+x /app.py

CMD ["/usr/bin/python", "/app.py"]
