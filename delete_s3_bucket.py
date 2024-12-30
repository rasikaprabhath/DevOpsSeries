import boto3
from botocore.exceptions import ClientError
import logging
import list_S3_buckets as lists3buckets

existings3client = lists3buckets.list_s3_buckets()


buckettodelete=input("Enter the bucket to delete : ")
client=boto3.client('s3')
for param in existings3client['Buckets']:
    print(f"Bucket Name : {param['Name']} :")
    if param["Name"]==buckettodelete:
        bucket=client.delete_bucket(
            Bucket=buckettodelete
        )
        print(f"Bucket {buckettodelete} sucessfully deleted")
        break
