FROM python:3

WORKDIR /app

COPY ai_engine.py .
COPY ml.py .
COPY firebase_init.py .
COPY model .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "ai_engine.py"]
