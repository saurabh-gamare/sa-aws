import boto3

# Using put_object (Used for small sized files like images)
bucket = boto3.client('s3')

with open('local_file.png', 'rb') as data:
    bucket.put_object(Bucket='bucket_name', Key='object_name', Body=data)


# Using upload_file (Used for large sized files)
# Using client
bucket = boto3.client('s3')

def upload_file(file_name, bucket_name, object_name=None, args=None):
    if object_name is None:
        object_name = file_name  # Use the file name as the object name

    bucket.upload_file(file_name, bucket_name, object_name, ExtraArgs=args)


# Using resource 
bucket = boto3.resource('s3')

def upload_file(file_name, bucket_name, object_name=None, args=None):
    if object_name is None:
        object_name = file_name  # Use the file name as the object name

    bucket.meta.client.upload_file(file_name, bucket_name, object_name, ExtraArgs=args)

