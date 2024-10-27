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
The test_main.py file is the test file of main.py which contain 3 test cases.
the test.csv is the test data for test cases.

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


# About lack of docker-compose.yaml file:

I know the file is like:

```
version: '3'

services:
  # Backend service
  web:
    image: python:3.9
    container_name: flask_app
    working_dir: /app
    volumes:
      - ./app:/app            # Mount local app directory to /app in the container
    ports:
      - "5000:5000"           # Map port 5000 on host to port 5000 in the container
    environment:
      - FLASK_ENV=development
      - MONGO_URI=mongodb://mongo:27017/mydatabase  # MongoDB connection URI
    command: flask run --host=0.0.0.0
    depends_on:
      - mongo                  # Ensures the web service starts after the database

  # Database service
  mongo:
    image: mongo:5
    container_name: mongo_db
    ports:
      - "27017:27017"          # Expose MongoDB's default port
    volumes:
      - mongo_data:/data/db    # Persist MongoDB data
  
volumes:
  mongo_data:
  ...
```

But I think I using file replace mongodb for the test, and it is not have web or restAPI service running in docker, so I do not think it have some meaningful to write additional docker-compose.yaml file.