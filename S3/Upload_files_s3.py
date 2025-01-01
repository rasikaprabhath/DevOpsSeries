import boto3
from botocore.exceptions import ClientError
import logging
import list_S3_buckets as s3buckets

#List all S3 Buckets in AWS. For thios we will import an object from the class list_S3_buckets.py

listbuckets=s3buckets.list_s3_buckets()

def upload_files(listbuckets):

    selectBucket = input("Enter the Bucket to upload files : ")
    pathname = input("Enter the full path of the file to be uploaded : ")
    filename = input("Enter the File Name")
    for param in listbuckets['Buckets']:
        if selectBucket == param["Name"]:
            client=boto3.client('s3')
            s3client=client.upload_file(pathname, selectBucket, filename)
            print(f"{filename} Sucessfully uploded ")

upload_files(listbuckets)