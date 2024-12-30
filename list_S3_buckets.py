# Retrieve the list of existing s3 buckets
import boto3
def list_s3_buckets():
    client = boto3.client('s3')
    s3cleint= client.list_buckets()
# Output the bucket names using the "Buckets" parameter
    print('Existing buckets are:')
    for param in s3cleint['Buckets']:
       print(f'Bucket Name : {param["Name"]} - Create Date & Time : {param["CreationDate"]}')
    return s3cleint
#invoking the bucket function
list_s3_buckets()