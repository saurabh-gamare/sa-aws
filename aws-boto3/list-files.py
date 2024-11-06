import boto3

bucket_name = ''

s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(bucket_name)

for obj in s3_bucket.objects.all():
    print(obj.key)