FROM python:3.9-slim

WORKDIR /firstapp

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /firstapp

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health