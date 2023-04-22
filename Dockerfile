FROM python:3
COPY . /Expension-tracker-app
WORKDIR /Expension-tracker-app
RUN pip3 install --upgrade setuptools
RUN pip3 install pysimplegui
EXPOSE 3333
CMD [ "python", "./main.py"]
