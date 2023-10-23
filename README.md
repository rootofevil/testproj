## Test Project

### Clone
```
git clone this_repo
cd this_repo
```

### Build
To build docker image run:
```
docker build -t {{your image tag}} .
docker login
docker push
```

### Run in Docker
```
docker run --rm -p 8000:8000 {{your image tag}}
```
service will be availble in http://127.0.0.1:8000

### Run in Kubernetes
In deployment.yaml change image parameter to your image tag.
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
Check you service to define url where service is available

## API Enpoints

* /attributes - return attributes of the image
* /thumbnail - return url of RGB thumbnail

### Requests examples
```
curl --location 'http://127.0.0.1:8000/attributes' --form 'file=@"/Users/user/example/S2L2A_2022-06-09.tiff"'
```
```
curl --location 'http://127.0.0.1:8000/thumbnail' --form 'file=@"/Users/user/example/S2L2A_2022-06-09.tiff"' \
--form 'dpi="100"'
```