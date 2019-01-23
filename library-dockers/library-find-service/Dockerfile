FROM python:3.7.2

WORKDIR /app
ADD app /app
RUN pip install -r ./requirements.txt

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["server.py"]