FROM ubuntu
RUN apt update
RUN apt install python3.10 -y
RUN apt install python3-pip -y
RUN pip3.10 install flask
RUN pip3.10 install pandas
COPY app1.py /proyecto/app1.py
COPY templates/index.html /proyecto/templates/index.html
COPY templates/login.html /proyecto/templates/login.html
COPY base_datos.csv /proyecto/base_datos.csv
COPY Contenedor_app2/app2.py /Contenedor_app2/app2.py
COPY Contenedor_app2/Dockerfile /Contenedor_app2/Dockerfile
WORKDIR /proyecto/
EXPOSE 80
CMD python3.10 /proyecto/app1.py