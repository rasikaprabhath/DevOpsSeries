import logging
import boto3
from botocore.exceptions import ClientError

#importing the list_S3_buckets.py file which was already written to list exisitng buckets
import list_S3_buckets as existings3
bucketname=existings3.list_s3_buckets()
print(bucketname)

#function to create a bucket
def create_s3_bucket():

    client=boto3.client('s3')
    try:
        newBucketName=input("enter a unique name to create the S3 bucket : ")
        if newBucketName!=bucketname:
            s3client=client.create_bucket(
                Bucket=newBucketName,
                CreateBucketConfiguration={
                    'LocationConstraint': 'ap-south-1'
                }
            )
        else:
            try:
                print(f"Given bucket {newBucketName} exists. Pls enter a new name")
                create_s3_bucket()
            except BucketAlreadyExists:
                print(f"Given bucket {newBucketName} exists. Pls enter a new name")
    except ClientError as e:
        logging.error(e)
        return False
        print(s3client)
    return True


create_s3_bucket()