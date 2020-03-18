# BigData-NYC-PV

This is first part of my project for Parking Violations.
There are several components that had to be created:
main.py,api.py, Dockerfile, requirements.txt and results.json


I had to run following commands in terminal:

docker build -t bigdata1:1.0 . <br/>
docker run -t bigdata1:1.0 python main.py <br/>
docker run -it bigdata1:1.0 /bin/bash <br/>
docker run -e APP_KEY=YOUR_APP_TOKEN -v $(pwd):/app bigdata:1.0 python main.py --page_size=1 --num_pages=11 --output=result.json <br/>
docker run -v $(pwd):/app -it bigdata1:1.0 /bin/bash <br/>
docker run -v $(pwd):/app -e APP_KEY= {Token obtained from nyc data open} -it bigdata1:1.0 python -m main --page_size=3 --num_pages=2 --output=results.json <br/>
docker tag 73e72f0c2332 dimitrijeadzic/bigdata1:1.0 <br/>
docker push dimitrijeadzic/bigdata1:1.0  <br/>


# BigData-Part2 - Loading Elastic Search

In folder Part 2 you can find documentation needed to get Parking Violations into ES.<br/>
To get things up and runing go into your folder in terminal and get docker running:<br/>

`docker-compose up -d`

After that run python program and push it into ES:<br/>

`sudo docker-compose run -e APP_KEY=Put-your-token-here -v $(pwd):/app bigdata python main.py --page_size=5 --num_pages=10 --output=result.json`

Adjust the **page size** and **page number** to your liking. It's better to have more data for vizualzasion purposes.
In place of **Put-your-token-here** put your own token.

You can chek if you have pushed data into ES Server properly run:


`curl -0 http://localhost:9200/_search?pretty`

Once you get this thing done you can move on to making interesting dashboars with **Kibana** by connecting to local host http://localhost:5601




