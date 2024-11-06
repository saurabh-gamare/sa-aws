"""
Shared Credential File: 
By default, Boto3 looks for a file named ~/.aws/credentials. 
You can specify multiple profiles in this file.

Example ~/.aws/credentials file:

    [default]
    aws_access_key_id = YOUR_ACCESS_KEY_ID
    aws_secret_access_key = YOUR_SECRET_ACCESS_KEY

    [profile_name]
    aws_access_key_id = ANOTHER_ACCESS_KEY_ID
    aws_secret_access_key = ANOTHER_SECRET_ACCESS_KEY

"""


import boto3

# Using resource
bucket = boto3.resource('s3')

response = bucket.create_bucket(
    Bucket = 'sa-bucket',
    ACL = 'private',                            # ACL: Access Control List, Values: 'public-read', 'public-read-write
    # CreateBucketConfiguration = {             # If the location is 'us-east-1', then no need to add here
    #     'LocationConstraint': 'us-east-1'
    # }
)

# Using client
bucket = boto3.client('s3')

response = bucket.create_bucket(
    Bucket = 'sa-bucket',
    ACL = 'private',                            
    # CreateBucketConfiguration = {            
    #     'LocationConstraint': 'us-east-1'
    # }
)