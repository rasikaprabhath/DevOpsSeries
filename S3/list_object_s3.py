import boto3
from botocore.exceptions import ClientError
import logging
import list_S3_buckets as s3buckets

#List all S3 Buckets in AWS. For thios we will import an object from the class list_S3_buckets.py

listbuckets=s3buckets.list_s3_buckets()

def list_files(listbuckets):


    for param in listbuckets['Buckets']:
        print(param["Name"])

    selectS3=input("Enter the S3 Bucket to view inside : ")
    if selectS3==param['Name']:
        s3client = boto3.client('s3')
        listfilesDic=s3client.list_objects(
            Bucket=selectS3
        )
        listfiles=listfilesDic["Contents"]
        length = len(listfiles)
        l=0
        for lf in listfiles:
            listcontent=listfiles[l]
            l=l+1
            print(listcontent["Key"])
    else:
        print("Invalid Bucket ")

list_files(listbuckets)