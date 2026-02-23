FROM python:3.9
WORKDIR /app
COPY lab2.2.py .
RUN pip install flask requests
EXPOSE 5001
CMD ["python", "lab2.2.py"]
