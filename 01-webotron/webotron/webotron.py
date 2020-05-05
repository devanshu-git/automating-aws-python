
import boto3
import click
from botocore.exceptions import ClientError

session=boto3.Session(profile_name='pythonprofile')
s3=session.resource('s3')

@click.group()
def cli():
       "We are deploying website to S3"
       print('hello')
@cli.command('list-buckets')
def list_buckets():
       "List all buckets"
       for bucket in s3.buckets.all():
              print(bucket)
@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
       "List objects within the bucket"
       for object in s3.Bucket(bucket).objects.all():
              print(object)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
       new_bucket='none'
       "This will setup bucket and host a website"
       try:
              new_bucket=s3.create_bucket(Bucket='bucket',
              CreateBucketConfiguration={ 'LocationConstraint': session.region_name})
       except ClientError as e:
              if e.response['Error']['Code']=='BucketAlreadyExists':
                     new_bucket=s3.Bucket(bucket)
                     print(new_bucket)
              else:
                     raise e

       policy='''{ 
            "Version": "2012-10-17", 
            "Statement": [ 
                { 
                   "Sid": "PublicReadGetObject", 
                    "Effect": "Allow", 
                   "Principal": "*", 
                    "Action": "s3:GetObject", 
                   "Resource": "arn:aws:s3:::%s/*" 
               } 
           ] 
        }'''%new_bucket.name
       policy=policy.strip()
       s3_policy=new_bucket.Policy()
       s3_policy.put(Policy=policy)

       bucket_website=new_bucket.Website()
       bucket_website.put( 
       WebsiteConfiguration={ 
           'IndexDocument': { 
             'Suffix': 'index.html' 
         }
           }
       )
       return


if __name__=='__main__':
       cli()
              


print('Above are all the buckets you asked for')


