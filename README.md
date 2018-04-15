# Formulating infrastructure on AWS:cloud: using Devops techniques

## Description:

## Setting up the project:

### :one: Creating users and miscellaneous stuff on AWS :cloud:

### :two: Installations

### :three: Creation and running the first instance on AWS :cloud: using AWS CLI
This is the first step in the project creation where we use aws-cli(command line interface) from our local systems to setup instances
on AWS cloud. Some sample commands to spin up the instances have been mentioned in the "" folder present in the main project folders.
The summary for the creation and running of the first instance is as follows:

1. Install aws cli
2. Type in "aws" on the console to test whether the installation was successful.
3. Configure the users for the particular user and region using "aws configure" command.
4. List out the users to see tat step 1 was completed successfully.
5. For building EC2 instance, we need the following details to setup using cli:
 - AMI(Amazon machine image) Id
 - Instance type
 - Security group
 - SSH key-pair
6. Creating security group
7. Opening ports access for SSH access on the security group
8. Describe the security groups configuration using various formats
9. Create SSH key-pair
10. Run the instance using aws-cli
11. Monitor the instance status
11. Querying the instance details such as dnsname etc.

### :four: Deploying webserver in :cloud: using AWS Cloudformation - Troposphere
This is the first step in the project creation where we use aws-cli(command line interface) from our local systems to setup instances
on AWS cloud. Some sample commands to spin up the instances have been mentioned in the "" folder present in the main project folders.
The summary for the creation and running of the first instance is as follows:

