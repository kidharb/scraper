FROM python:alpine3.20
COPY . /scraper
WORKDIR /scraper
RUN pip install -r requirements.txt
EXPOSE 5555
CMD ["python", "./scraper.py"]
