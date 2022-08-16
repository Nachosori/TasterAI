FROM python:3.9

EXPOSE 8501

WORKDIR /tasteraiapp

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

COPY . .

ENV PORT=8501

CMD streamlit run  --server.enableXsrfProtection false --server.enableCORS false --server.port ${PORT}  main.py
