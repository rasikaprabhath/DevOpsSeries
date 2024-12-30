import logging
import boto3
from botocore.exceptions import ClientError
import botocore.errorfactory

#importing the list_S3_buckets.py file which was already written to list exisitng buckets
import list_S3_buckets as existings3
s3cleintexisting=existings3.list_s3_buckets()


#function to create a bucket
def create_s3_bucket(s3cleintexisting):

    client=boto3.client('s3')
    try:
        newBucketName=input("enter a unique name to create the S3 bucket : ")
        for param in s3cleintexisting['Buckets']:


            try:
                if newBucketName!=param["Name"]:
                    s3client=client.create_bucket(
                        Bucket=newBucketName,
                        CreateBucketConfiguration={
                            'LocationConstraint': 'ap-southeast-1'
                        }
                    )
                    print(f'Bucket {newBucketName} Sucessfully Created')
                    print("")

                else:
                    print("This Bucket already exists in your Account. Pls enter a globally unique name ")
                    create_s3_bucket(s3cleintexisting)
            except botocore.errorfactory.ClientError:
                print("Bucket cannot be created. Pls enter a globally unique name ")
                return False
            return False

    except ClientError as e:
        logging.error(e)
        return False

    return True


create_s3_bucket(s3cleintexisting)