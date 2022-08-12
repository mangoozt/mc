import os
import sys

import boto3

if __name__ == "__main__":
    session = boto3.session.Session()
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
        endpoint_url='https://storage.yandexcloud.net'
    )
    filename = sys.argv[1]
    file_key = os.path.basename(filename)

    s3.upload_file(filename, os.getenv('S3_BUCKET'), file_key)
