import boto3
from botocore.exceptions import ClientError
import logging
import list_S3_buckets as s3buckets
import os

#List all S3 Buckets in AWS. For thios we will import an object from the class list_S3_buckets.py

listbuckets=s3buckets.list_s3_buckets()

def upload_files(listbuckets):

    selectBucket = input("Enter the Bucket to upload files : ")
    filename = input("Enter the File Name")
    pathname = input("Enter the full path of the file to be uploaded : ")
#extracting the last part of the string sepreated by"\"

    filefrompath=os.path.basename(pathname).split("'\'")[-1]
#checking the last string part extracted from th epath has a file associated with it as a file name should ave a extension seperated by a "."

    if "." in filefrompath:
        print(filefrompath)
    else:
        print("path does not have a file. But will take the already enterd file name as the valid file and upload it to the S3 Bucket")
#removes the leading and trailing spaces in the string assinged to file name by strip()
        pathname=pathname+"\\"+ filename.strip()
        print(pathname)


    for param in listbuckets['Buckets']:
        try:
            if selectBucket == param["Name"]:
                client=boto3.client('s3')
                s3client=client.upload_file(pathname, selectBucket, filename)
                print(f"{filename} Sucessfully uploded ")
        except PermissionError:
            return False
        except ClientError as e:
            logging.error(e)
            return False



upload_files(listbuckets)