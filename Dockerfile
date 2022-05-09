FROM python

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "test.py"]
