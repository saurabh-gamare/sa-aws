import boto3

# Using client
bucket = boto3.client('s3')

response = bucket.list_buckets()

for data in response['Buckets']:
    print(data['Name'])



# Using resource
bucket = boto3.resource('s3')

response = bucket.buckets.all()

for data in response:
    print(data.name)