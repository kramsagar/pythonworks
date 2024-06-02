import boto3


session = boto3.Session(
        aws_access_key_id='AKIA47CRYX73SLBEHN4G',
    aws_secret_access_key='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',
    region_name='us-east-1'
    )

ec2 = session.client("ec2")

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()
#print('Regions:', response['Regions'])

for i in response['Regions']:
    print(i.get("RegionName"))
    ec2region = session.client("ec2",region_name=i.get("RegionName"))
    print(ec2region.describe_regions())

