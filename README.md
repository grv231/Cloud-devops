# Infrastructure on AWS :cloud: using Devops techniques

## Description:

## Setting up the project:

### :one: Creating users and miscellaneous stuff on AWS :cloud:

### :two: Installations

#### Installing AWS CLI

#### Installing Python Troposhere

### :three: Creation and running the first instance on AWS :cloud: using AWS CLI
This is the first step in the project creation where we use aws-cli(command line interface) from our local systems to setup instances
on AWS cloud. Some sample commands to spin up the instances have been mentioned in the "" folder present in the main project folders.
The summary for the creation and running of the first instance is as follows:

1. Install aws cli
2. Type in "aws" on the console to test whether the installation was successful.
3. Configure the users for the particular user and region using "aws configure" command.
4. For building EC2 instance, we need the following details to setup using cli:
  - AMI(Amazon machine image) Id
  - Instance type
  - Security group
  - SSH key-pair
6. Creating security group and opening ports access for SSH access on the security group
7. Create SSH key-pair
8. Run the instance using aws-cli
9. Monitoring and querying the instance details such as dnsname etc.
10. SSH into the instance, create an html page to check its working.
11. Terminate the instance using aws cli.

### :four: Deploying webserver in :cloud: using AWS Cloudformation - Troposphere and Ansible
This is the second step where we deploy instances and setup infrastrcuture automatically using **AWS Cloudformation**. For this project, we are using the **Python Troposphere** to create the Cloudformation stack template. We follow the practices of IaC (Infastructure as Code) using the troposphere library and json configuration. We are using **JSON-YAML** template here to create our infrastructure.

The steps for creating the template is as follows:


### :five: Incorporating devops using CD/CI practices - Jenkins
This is the second step where we deploy instances and setup infrastrcuture automatically using **AWS Cloudformation**. For this project, we are using the **Python Troposphere** to create the Cloudformation stack template. We follow the practices of IaC (Infastructure as Code) using the troposphere library and json configuration. We are using **JSON-YAML** template here to create our infrastructure.
