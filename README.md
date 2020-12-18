# This is a simple docker flask app

## Build image
```
docker build -f Dockerfile -t docker:flask .
```

## Run container
```
docker run -p 9001:9001 -v /home/ubuntu/demo/:/usr/src/app/static/ -ti docker:flask python3 app.py
```
this will put container port 9001 to host port 9001. Images uploaded to flask /usr/src/app/static/ folder will be saved to local host at /home/ubuntu/demo/