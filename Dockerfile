FROM python:3
# FROM kubernetes import client
# FROM kubernetes import config
FROM registry.access.redhat.com/ubi8/python-36

USER root
RUN yum update-minimal --security --sec-severity=Important --sec-severity=Critical --disableplugin=subscription-manager -y && rm -rf /var/cache/yum
RUN yum update libnghttp2 kernel-headers gnutls git systemd-libs systemd-pam systemd --disableplugin=subscription-manager -y && rm -rf /var/cache/yum
RUN yum -y remove nodejs && rm -rf /var/cache/yum
USER 1001


# Licence needs to added when we get it for 1.4 release
# COPY /licenses/LA_en /licenses/LA_en

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip3 --no-cache-dir install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["main.py"]
