from troposphere import Ref, Template, Parameter, Output, Join, GetAtt, Base64
import troposphere.ec2 as ec2

# Create the template object
t = Template()

# Add security group 
# Add ssh Key pair
# Add ami-id and instance type

sg = ec2.SecurityGroup("LampSg")
sg.GroupDescription = "Allow access to ports 80 and 22 to EC2 server"

# Setup the ports access for security groups
sg.SecurityGroupIngress = [
    ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort = "22", ToPort = "22", CidrIp = "0.0.0.0/0"),
    ec2.SecurityGroupRule(IpProtocol = "tcp", FromPort = "80", ToPort = "80", CidrIp = "0.0.0.0/0"),
]

# Informing the security group add resources to the template
# This is a method of Troposphere library, not cloudformation
t.add_resource(sg)

# Periodically cehck whether the code is correct or not
print(t.to_json())

# Adding ssh Keypair externally as cannot be generated here
# These variables are NOT cloudformation attributes
keypair = t.add_parameter(Parameter(
        "KeyName",
        Description = "Name of SSH keypair that will be used to access the instance",
        Type = "String"
    ))

# Creating an instance variable for EC2 deployment
instance = ec2.Instance("webserver")
instance.ImageId = "ami-824c4ee2"
instance.InstanceType = "t2.micro"

# Using the Ref module of troposphere for list values of various attributes
# Ref is defined in the Cloudformation template documentation
instance.SecurityGroups = [Ref(sg)]
instance.KeyName = Ref(keypair)

# User data section for running bash scripts on instance after instance creation
# Encoding binary data to Base 64 for successful transfer
ud = Base64(Join("\n", 
    [
        "#!/bin/bash",
        "sudo yum -y install httpd",
        "sudo service httpd start",
        "sudo chkconfig httpd on",
        "sudo echo '<html><body><h1>Welcome to Devops on AWS</h1><h2>Testing the commits</h2></body><html>' > /var/www/html/test.html"
    ]))

            
instance.UserData = ud

# Add the instance resources to the template
t.add_resource(instance)

# Adding output for better user experience
t.add_output(Output(
        "InstanceAccess",
        Description = "Command to access the instance using SSH",
        
        #Join function comes from Cloudformation to join separate strings together
        # GetAtt function is also given to us by Cloudformation
        Value = Join("",["ssh -i ~/.ssh/LampKey.pem ec2-user@",GetAtt(instance,"PublicDnsName")])
))

# This is used to output URL of the webserver
t.add_output(Output(
        "WebUrl",
        Description = "The URL of webserver",
        Value = Join("",["http://",GetAtt(instance,"PublicDnsName")])
))

print(t.to_json())