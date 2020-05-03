# coding: utf-8
import boto3
session=boto3.Session(profile_name='pythonprofile')
session
s3=session.resource('s3')
s3
