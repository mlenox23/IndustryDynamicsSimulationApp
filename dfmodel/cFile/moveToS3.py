
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import logging
import boto3
from botocore import UNSIGNED
from botocore.config import Config
from botocore.exceptions import ClientError
from datetime import datetime
import ebdjango.settings as settings


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then same as file_name
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    ACCESS_KEY = ""
    SECRET_KEY = ""
    # Upload the file
    # signature_version=UNSIGNED, 
    # s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))
    s3_client = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    # s3_client = boto3.client('s3', config=Config(region_name = settings.AWS_S3_REGION_NAME, aws_access_key_id=settings.AWS_ACCESS_KEY_ID, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY))
    try:
        print("uploading " + str(file_name))
        response = s3_client.upload_file(file_name, bucket, object_name)

        s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        object_acl = s3.ObjectAcl(bucket,object_name)
        response = object_acl.put(ACL='public-read')
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    """Exercise upload_file()"""

    # Set these values before running the program
    bucket_name = 'dardendifferentialmodeloutput'
    now = datetime.now()
    # object_name = now.strftime("%d/%m/%Y %H:%M:%S") +" output.txt"
    object_name = now.strftime("%d-%m-%Y %H:%M:%S") + " output.txt"
    file_name = 'output1.txt'
   
    stats_bucket_name = "nk-cournot-stats"
    stats_file_name = now.strftime("%d-%m-%Y %H:%M:%S") + " stats.txt"
    logging.info("uploading stats file name " + str(stats_file_name))
    stats_file = "stats.txt"
    # Set up logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Upload raw output file
    response = upload_file(file_name, bucket_name, object_name)
    if response:
        logging.info('Raw output file was uploaded')

    # Upload stats file
    stats_response = upload_file(stats_file, stats_bucket_name, stats_file_name)
    if stats_response:
        logging.info('Statistics file was uploaded')


if __name__ == '__main__':
    main()


