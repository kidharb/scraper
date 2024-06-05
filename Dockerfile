FROM python:alpine3.20
RUN mkdir -p /scraper
COPY scraper.py requirements.txt /scraper
WORKDIR /scraper
RUN pip install -r requirements.txt
EXPOSE 5555
CMD ["python", "./scraper.py"]
