# Credit Card Default Prediction

### Problem Statement

Financial threats are displaying a trend about the credit risk of commercial banks as the
incredible improvement in the financial industry has arisen. In this way, one of the
biggest threats faces by commercial banks is the risk prediction of credit clients. The
goal is to predict the probability of credit default based on credit card owner's
characteristics and payment history.

### Approach: 
The classical machine learning tasks like Data Exploration, Data Cleaning,
Feature Engineering, Model Building and Model Testing. Try out different machine
learning algorithms that’s best fit for the above case.


### Tech Stack Used

 - Python
 - MongoDB
 - GitHub Action
 - Docker
 - Machine Learning


## How to run?

Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.


## Data Collections
![image](https://github.com/Abdul-Jaweed/Customer-Personality-Analysis/blob/main/flowchart/1.png)



## Project Archietecture
![image](https://github.com/Abdul-Jaweed/Customer-Personality-Analysis/blob/main/flowchart/2.png)


## Deployment Archietecture
![image](https://github.com/Abdul-Jaweed/Customer-Personality-Analysis/blob/main/flowchart/3.png)



### Step 1: Clone the repository
```bash
git clone https://github.com/Abdul-Jaweed/Credit-Card-Default-Prediction.git
```


### Step 2- Create a conda environment after opening the repository

```bash
conda create -p venv  python=3.8.15 -y
```

```bash
conda activate venv/
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```


### Step 5 - Run the application server
```bash
python app.py
```



## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

then run 
```
python main.py
```