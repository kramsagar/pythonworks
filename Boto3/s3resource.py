import boto3


#custom_credential_path = '.\\.aws\\credentials'
#custom_config_path = '.\\.aws\\config'

session = boto3.Session(
        aws_access_key_id='AKIA47CRYX73SLBEHN4G',
    aws_secret_access_key='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',
    region_name='us-east-1'
    )

s3resource = session.client("s3")

print(s3resource.list_buckets())

for i in s3resource.list_buckets():
    print(i)
    print("=======================")

print("=======================")

for bucket in s3resource.list_buckets().get("Buckets"):
    print(bucket.get("Name"))

"""
(.venv) PS D:\mydrive\DevopsWorks\PythonWork\Boto3> python .\s3resource.py
{'ResponseMetadata': {'RequestId': 'VQ12QC5VWNF65VWF', 'HostId': 'dwHL4smK505xkJoSkMWU52ePmN4brUOa+U6ZRM2LXW3ooPn0rN32MHU7R/XRkFAeDx96zUpvW1I=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'dwHL4smK505xkJoSkMWU52ePmN4brUOa+U6ZRM2LXW3ooPn0rN32MHU7R/XRkFAeDx96zUpvW1I=', 'x-amz-request-id': 'VQ12QC5VWNF65VWF', 'date': 'Sat, 01 Jun 2024 05:33:03 GMT', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Buckets': [{'Name': 'losmybucket', 'CreationDate': datetime.datetime(2024, 6, 1, 5, 4, 30, tzinfo=tzutc())}, {'Name': 'pgsmybucket', 'CreationDate': datetime.datetime(2024, 6, 1, 5, 4, 43, tzinfo=tzutc())}], 'Owner': {'DisplayName': 'lab-aws+LabServices-prod-9515', 'ID': 'e3b3d5cc70afddf93987bb75cd34aedff58823d10b95d6a6dc6912097b745fcc'}}
ResponseMetadata
=======================
Buckets
=======================
Owner
=======================
=======================
losmybucket
pgsmybucket
(.venv) PS D:\mydrive\DevopsWorks\PythonWork\Boto3> 

"""
    








