
import boto3
import click

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

if __name__=='__main__':
       cli()
              


print('Above are all the buckets you asked for')


