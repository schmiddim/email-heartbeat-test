FROM python:3.8-slim

COPY *py  ./
ENTRYPOINT ["python3", "check_inbox.py"]
