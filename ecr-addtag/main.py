# coding: utf-8
import argparse
import logging
import sys
from botocore.exceptions import ClientError
from boto3 import Session

logging.getLogger("botocore").setLevel(logging.WARNING)
logger = logging.getLogger()
logger.setLevel(logging.INFO)



class AwsUtils(object):
    def __init__(self, access_key, secret_key, region='us-east-1'):
        session = Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
        self.ecr = session.client('ecr')

    def get_image_manifest(self, registory_id: str, repository: str, source_tag: str) -> str:
        response = self.ecr.batch_get_image(registryId=registory_id, repositoryName=repository, imageIds=[{'imageTag': source_tag}])
        failures = response.get('failures')
        if failures:
            raise Exception("Cluster '%s' is %s" % (cluster, failures[0].get('reason')))
        return response.get('images')[0].get('imageManifest')

    def add_tag(self, registory_id: str, repository: str, add_tag: str, image_manifest:str):
        try:
            response = self.ecr.put_image(registryId=registory_id, repositoryName=repository, imageManifest=image_manifest, imageTag=add_tag)
        except ClientError as e:
            if e.response['Error']['Code'] == 'ImageAlreadyExistsException':
                logger.info('Image Tag already Exists')
                pass
            else:
                raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ecr add tag')
    parser.add_argument('--key', default="")
    parser.add_argument('--secret', default="")
    parser.add_argument('--region', default='us-east-1')
    parser.add_argument('--registory-id', default='', required=True)
    parser.add_argument('--repository', default='', required=True)
    parser.add_argument('--source-tag', default='', required=True)
    parser.add_argument('--add-tag', default='', required=True)
    argp = parser.parse_args()
    
    awsutils = AwsUtils(access_key=argp.key, secret_key=argp.secret, region=argp.region)
    image_manifest = awsutils.get_image_manifest(registory_id=argp.registory_id, repository=argp.repository, source_tag=argp.source_tag)
    awsutils.add_tag(registory_id=argp.registory_id, repository=argp.repository, add_tag=argp.add_tag, image_manifest=image_manifest)