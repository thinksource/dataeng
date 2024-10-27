# How to run:
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

# How to test
```
python -m unittest 
```

# Some correct



    """

    Add a new column named SalaryBucket to categorize the employees based on their salary as follows:
        A for employees earning below 50.000
        B for employees earning between 50.000 and 100.000
        C for employees earning above 100.000
    """


I think the number should be 50,000 and 100,000 not 50 and 100, if 50 and 100 the number may be too small and all employees get category C.
