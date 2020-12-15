# Industry Dynamics Simulation

This model simulates the evolution of an industry over time as firms enter, compete, grow, and exit. At the heart of the model is a production function that allows for interdependency (K) between a finite and discrete set of productive activities (N). As N and K increase, the production function becomes complex thus prohibiting analytical optimization and necessitating the search for favorable onfigurations of productive activities that increase firm profits. The profit function, itself, becomes non-linear and resembles a rugged landscape with numerous maxima.

The model configurations below refer to the nature of market competition simulated. For example, the Cournot Model simulates a market where firms create commodity products undifferentiated in quality or type and where firms compete based solely on cost. The Vertical Differentiation Model allows firms to differentiate based on quality but not type, resulting in firms varying their prices with their quality levels. Look for additional market models as they are developed.

References:
1. Lenox, Michael, Scott Rockart, & Arie Lewin. 2007. “Interdependency, Competition, and Industry Dynamics.” Management Science. 53(4): 599-615.
2. Lenox, Michael, Scott Rockart, & Arie Lewin. 2006. “Interdependency, Competition, and the Distribution of Firm and Industry Profits.” Management Science. 52(5): 757-772.


# Instructions to install and run the app locally 

Industrial Dynamics Simulation App is built by using python Django framework. 

1. Install Django, build-essentials, python3, python3-pip
2. Install aws-cli and configure AWS secret and access key 
3. Install all libraries present in requirements.txt 
4. Run the app - python manage.py runserver 0.0.0.0:8002 


## Dockerized app
You can run the app as a Docker app 

1. Install docker, docker-compose
2. In the project folder that contains 'Dockerfile' and 'docker-compose.yml' files, run the following command - "docker-compose build" to build the docker image, and 'docker-compose up' to run the containerized app. 

Additionally images are also stored in AWS ECR (Amazon's container registry), and can be used to run the app locally as well. 
Here there are two containers - one to run the UI and Business logic, one to run the C program and upload the output to S3 bucket. 

```
version: '2'

services:
  web:
    image: 129703625756.dkr.ecr.us-east-1.amazonaws.com/michael_darden:latest
    command: python manage.py runserver 0.0.0.0:8002
    ports:
      - 8002:8002
    networks:
      - nk-network
  nk-model:
    image: 129703625756.dkr.ecr.us-east-1.amazonaws.com/nk-model:latest
    ports:
      - 5000:5000
    networks:
      - nk-network

networks:
  nk-network:
    driver: bridge

```