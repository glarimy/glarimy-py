FROM python:3.7.2

WORKDIR /app
ADD . /app
RUN pip install -r ./requirements.txt

EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]