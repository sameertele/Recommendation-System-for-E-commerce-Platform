#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import os
import paramiko
from scp import SCPClient

def create_scp_client(ssh_client):
    return SCPClient(ssh_client.get_transport())

def deploy_model():
    ec2_instance_id = 'i-0abcd1234efgh5673'  
    ec2_region = 'us-east-2'  
    s3_bucket_name = 'bucket1'  
    model_local_path = 'models/recommendation_model'  
    s3_model_path = 'models/recommendation_model' 

    ec2 = boto3.resource('ec2', region_name=ec2_region)
    s3 = boto3.client('s3')

    print(f"Uploading model from {model_local_path} to S3 bucket {s3_bucket_name} at {s3_model_path}")
    s3.upload_file(model_local_path, s3_bucket_name, s3_model_path)

    instance = ec2.Instance(ec2_instance_id)
    
    if instance.state['Name'] != 'running':
        print(f"Starting EC2 instance {ec2_instance_id}")
        instance.start()
        instance.wait_until_running()
        print(f"EC2 instance {ec2_instance_id} is now running")

    ec2_public_ip = instance.public_ip_address

    ssh_key_path = 'private'  
    ec2_username = 'private'  

    print(f"Connecting to EC2 instance {ec2_instance_id} at {ec2_public_ip}")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ec2_public_ip, username=ec2_username, key_filename=ssh_key_path)

   
    scp = create_scp_client(ssh_client)
    scp.get(f"s3://{s3_bucket_name}/{s3_model_path}", 'model/deployed_model')  

    
    commands = [
        "sudo yum update -y",
        "pip install -r requirements.txt",  
        "mkdir -p /home/ec2-user/models",
        "mv model/deployed_model /home/ec2-user/models/recommendation_model",
        
    ]
    
    print("Executing setup commands on EC2 instance")
    for command in commands:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        print(stdout.read().decode())
        print(stderr.read().decode())

    ssh_client.close()
    scp.close()

    print("Model deployed successfully!")

if __name__ == "__main__":
    deploy_model()

