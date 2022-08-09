#
# File: s3-ref.py
# Auth: Martin Burolla
# Date: 7/26/2022
# Desc: Main entry point for the Python S3 reference guide.
#


import data_access_s3
import boto3
import data_access_s3
from botocore.exceptions import ClientError


def main():
    # Upload
    print(data_access_s3.upload_to_s3())

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file("uploadme.txt", 'siu-avb-bucket', 'upload_stu7_file.txt')
    except ClientError as e:
        print(e)
        return False
    return True



    # Download
    # data_access_s3.download_from_s3()


if __name__ == '__main__':   # dunder
    main()
