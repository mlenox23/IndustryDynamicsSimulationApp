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
from botocore.exceptions import ClientError
from datetime import datetime


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

    # Upload the file
    s3_client = boto3.client('s3')

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def main():
    now = datetime.now()
    # Set these values before running the program
    bucket_name = 'dardendifferntialmodeloutput'
    #file_name = now.strftime("%d/%m/%Y %H:%M:%S") + " output.txt"
    file_name = now.strftime("%d-%m-%Y %H:%M:%S") + " output.txt"
    object_name = 'output1.txt'

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
    stats_response = upload_file(stats_file_name, stats_bucket_name, stats_file)
    if stats_response:
        logging.info('Statistics file was uploaded')


if __name__ == '__main__':
    main()
