from __future__ import print_function
import boto3

client = boto3.client('ec2')
instance_info = client.describe_instances()

print(instance_info)
