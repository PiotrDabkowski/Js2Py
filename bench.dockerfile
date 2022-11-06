FROM python:3.11-alpine
WORKDIR /app
RUN pip3 install pyjsparser six
RUN pip3 install tzlocal
RUN apk add --update alpine-sdk
RUN apk --no-cache --update add build-base
RUN pip3 install numpy

ADD . /app

RUN ls
#CMD ["python3", "js2py/utils/injector.py"]
CMD ["python3", "simple_test.py"]