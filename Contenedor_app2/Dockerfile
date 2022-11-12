FROM ubuntu
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN pip3.10 install flask
RUN pip3.10 install pandas
COPY app2.py /proyecto/app2.py
WORKDIR /proyecto/
EXPOSE 80
CMD python3.10 /proyecto/app2.py