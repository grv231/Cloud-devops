# Infrastructure on AWS :cloud: using Devops techniques

## Description:

## Setting up the project:

#### Variables for AWS CLI sub-project

#### Variables for Dynamic Inventory AWS sub-project
- export AWS_ACCESS_KEY_ID='Your ID'
- export AWS_SECRET_ACCESS_KEY='Your AccessKey'
- export EC2_INI_PATH=/etc/ansible/ec2.ini
- export ANSIBLE_HOSTS=/etc/ansible/ec2.py

*Better to keep all the variables in the bashrc file so that it can be initiated at the start of virtual machine: cd ~/.bashrc* 

### :one: Creating users and miscellaneous stuff on AWS :cloud:

### :two: Installations (Pre-requisites)
- Install Python (if not present)
- Install AWS CLI
- Install Python Troposhere library
- Install Ansible
- Install Boto library

### :three: Creation and running the first instance on AWS :cloud: - *AWS CLI*
This is the first step in the project creation where we use aws-cli(command line interface) from our local systems to setup instances
on AWS cloud. Some sample commands to spin up the instances have been mentioned in the "" folder present in the main project folders.
The summary for the creation and running of the first instance is as follows:

1. Install aws cli
2. Type in "aws" on the console to test whether the installation was successful.
3. Configure the users for the particular user and region using "aws configure" command.
4. For building EC2 instance, we need the following details to setup using cli:
    + AMI(Amazon machine image) Id
    + Instance type
    + Security group
    + SSH key-pair
6. Creating security group and opening ports access for SSH access on the security group
7. Create SSH key-pair
8. Run the instance using aws-cli
9. Monitoring and querying the instance details such as dnsname etc.
10. SSH into the instance, create an html page to check its working.
11. Terminate the instance using aws cli.

### :four: Create and deploying web-server in :cloud: using AWS Cloudformation - *Troposphere and Ansible*
This is the second step where we deploy instances and setup infrastrcuture automatically using **AWS Cloudformation**. For this project, we are using the **Python Troposphere** to create the Cloudformation stack template. We follow the practices of IaC (Infastructure as Code) using the troposphere library and json configuration. We are using **JSON-YAML** template here to create our infrastructure.

**Basic Infrastructure**:
 - The file is kept in the folder **"cloudformation-template"** named *web-server.py*
 - Create a template file using the command: *python web-server.py > web-server.template*
 - Navigate to the AWS Cloudformation service in AWS GUI and create a new stack
 - Create the stack by uploading the template to S3 bucket using the option "upload template to S3"
 - Provide appropriate stack names and keynames
 - Create the stack. Track the changes using *Status* and *Output* tabs
 - Using the *Output* tab of AWS Cloudformation, we can SSH into the instance or we can even check our HTML working code.
    
**Infrastructure using Dynamic AWS inventory file and Ansible**:
 - Following the instructions of AWS dynamic inventory file, first we download the file using wget
 - Navigate to the path **/etc/ansible**. Download the *ec2.py* file using two resources:
    + Either download using: **sudo wget <a href=http://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py>link</a>**
    + Or use the file directory from the folder *dynamic-inventory-AWS*
 - Download the *ec2.ini* configuration file in the **/etc/ansible** using two resources:
    + Either download using: **sudo wget <a       href=http://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini>link</a>**
    + Or use the configuration file directory from the folder *dynamic-inventory-AWS*
 - Change the permissions on the *ec2.py* file using executable permissions for the user
 - Change the *ec2.ini* configutation file to include only for the region we are interested in. In this project, its us-west-1. Comment out rest of the regions for exclusion
 - Use the command **./ec2.py --list** to query actual AWS resource, provided the variables for AWS access Key and ID was fixed before.
 - Run the first ansible command:
    **ansible --private-key ~/.ssh/"YourKeyName".pem --user=ec2-user -m ping all**
 - (OPTIONAL) We can modify the SSH options to shorten the above command using a config file
    + Create a config file inside ssh using: **vim ~/.ssh/config**
    + Add the following lines (all in new lines):
        IdentityFile ~/.ssh/"YourKeyName".pem
        User ec2-user
        StrictHostKeyChecking no
        PasswordAuthentication no
    + *Remember, this technique is good if there one dedicated machine for using Ansible*
 - Run the command: **ansible -m ping all** to achieve the same effect
 - Create a playbook called "lamp_initial.yml" for spinning up servers in EC2 instance. 
   Run the playbook using: **ansible-playbook lamp_initial.yml**
 ```yml
 ---
- hosts: all
  become: yes
  tasks:
    - name: Install Apache2 webserver
      yum: name=httpd state=present
    - name: Ensure apache is up and running
      service: name=httpd state=started enabled=yes
```
- To do the same operation without ansible tasks, we can individually build **ansible roles** for implementing DRY principles
- In the directory /etc/ansible, make a folder *roles* to define roles for individual servers
- Create the role for php and apache using:
    + ansible-galaxy init php
    + ansible-galaxy init apache
- Navigate to the *tasks* folder of the roles. Documentation has been provided in the **roles** folder of this repository

 
 

### :five: Incorporating devops using CD/CI practices - *Ansible, Jenkins and PHPUnit test*
This is the second step where we deploy instances and setup infrastrcuture automatically using **AWS Cloudformation**. For this project, we are using the **Python Troposphere** to create the Cloudformation stack template. We follow the practices of IaC (Infastructure as Code) using the troposphere library and json configuration. We are using **JSON-YAML** template here to create our infrastructure.
