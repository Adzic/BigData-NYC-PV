# BigData-NYC-PV

This is first part of my project for Parking Violations.
There are several components that had to be created.
main.py,api.py, Dockerfile, requirements.txt and results.json


I had to run following commands in terminal:

docker build -t bigdata1:1.0 .
docker build -t bigdata1:1.0 .
docker run -t bigdata1:1.0 python main.py
docker run -t bigdata1:1.0 python main.py
docker run -it bigdata1:1.0 /bin/bash
docker run -e APP_KEY=YOUR_APP_TOKEN -v $(pwd):/app bigdata:1.0 python main.py --page_size=1 --num_pages=11 --output=result.json
docker run -v $(pwd):/app -it bigdata1:1.0 /bin/bash
docker run -v $(pwd):/app -e APP_KEY= {Token obtained from nyc data open} -it bigdata1:1.0 python -m main --page_size=3 --num_pages=2 --output=results.json
docker tag 73e72f0c2332 dimitrijeadzic/bigdata1:1.0
docker push dimitrijeadzic/bigdata1:1.0 
