## Deploying a model as a web-service

* Create a virtual environment
* Create a prediction script
* Put the script in a flask app
* Package the app to docker



```bash
docker build -t ride-duration-prediction-service:v1 .
```

```bash
docker run -it --rm -p 9696:9696 ride-duration-prediction-service
```