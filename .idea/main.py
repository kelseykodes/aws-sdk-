#
# File: s3-ref.py
# Auth: Martin Burolla
# Date: 7/26/2022
# Desc: Main entry point for the Python S3 reference guide.
#


import data_access_s3
import boto3

def main():
    # Upload
    print(data_access_s3.upload_to_s3())

    # Download
    # data_access_s3.download_from_s3()


if __name__ == '__main__':   # dunder
    main()
