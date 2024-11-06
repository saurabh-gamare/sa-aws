import boto3

bucket_name = ''

bucket = boto3.resource('s3')

s3_object = bucket.Object(bucket_name, 'file.pdf')

s3_object.download_file('downloaded.pdf')