* How to run:
1, if you have docker on your machine: just build docker image:
```
docker build -t codet:v1.0 .
```
and then run the image with fetch output folder of docker instance:

```
docker run --rm -v .:/app/output codet:v1.0
```
and it will genereate data.json file while the json file is the result of you want.

2, use local python to run:
```
python main.py
```
it will generate the ./output/data.json file, and it is the result of you want.

* How to test
```
python -m unittest 
```

# Some correct
