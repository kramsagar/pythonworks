import boto3


#custom_credential_path = '.\\.aws\\credentials'
#custom_config_path = '.\\.aws\\config'

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

"""
(.venv) PS D:\mydrive\DevopsWorks\PythonWork\Boto3> python .\Ec2instance2.py
ap-south-1
Traceback (most recent call last):
  File "D:\mydrive\DevopsWorks\PythonWork\Boto3\Ec2instance2.py", line 22, in <module>
    print(ec2region.describe_regions())
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\mydrive\DevopsWorks\PythonWork\.venv\Lib\site-packages\botocore\client.py", line 565, in _api_call
    return self._make_api_call(operation_name, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\mydrive\DevopsWorks\PythonWork\.venv\Lib\site-packages\botocore\client.py", line 1021, in _make_api_call
    raise error_class(parsed_response, operation_name)
botocore.exceptions.ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeRegions operation: You are not authorized to perform this operation. User: arn:aws:iam::891377205239:user/cloud_user is not authorized to perform: ec2:DescribeRegions with an explicit deny in a service control policy
(.venv) PS D:\mydrive\DevopsWorks\PythonWork\Boto3> 
"""




# Retrieves availability zones only for region of the ec2 object
response = ec2.describe_availability_zones()
#print('Availability Zones:', response['AvailabilityZones'])


"""
Regions: [{'Endpoint': 'ec2.ap-south-1.amazonaws.com', 'RegionName': 'ap-south-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-north-1.amazonaws.com', 'RegionName': 'eu-north-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-west-3.amazonaws.com', 'RegionName': 'eu-west-3', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-west-2.amazonaws.com', 'RegionName': entral-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.sa-east-1.amazonaws.com', 'RegionName': 'sa-east-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-southeast-1.amazonaws.com', 'RegionName': 'ap-southeast-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-southeast-2.amazonaws.com', 'RegionName': 'ap-southeast-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-central-1.amazonaws.com', 'RegionName': 'eu-central-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-east-1.amazonaws.com', 'RegionName': 'us-east-1', 'entral-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.sa-east-1.amazonaws.com', 'RegionName': 'sa-east-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-southeast-1.amazonaws.com', 'RegionName': 'ap-southeast-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.ap-southeast-2.amazonaws.com', 'RegionName': 'ap-southeast-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.eu-central-1.amazonaws.com', 'RegionName': 'eu-central-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-east-1.amazonaws.com', 'RegionName': 'us-east-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-east-2.amazonaws.com', 'RegionName': 'us-east-2', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-west-1.amazonaws.com', 'RegionName': 'us-west-1', 'OptInStatus': 'opt-in-not-required'}, {'Endpoint': 'ec2.us-west-2.amazonaws.com', 'RegionName': 'us-west-2', 'OptInStatus': 'opt-in-not-required'}]
Availability Zones: [{'State': 'available', 'OptInStatus': 'opt-in-not-required', 'Messages': [], 'RegionName': 'us-east-1', 'ZoneName': 'us-east-1a', 'ZoneId': 'use1-az6', 'GroupName': 'us-east-1', 'NetworkBorderGroup': 'us-east-1', 'ZoneType': 'availability-zone'}, {'State': 'available', 'OptInStatus': 'opt-in-not-required', 'Messages': [], 'RegionName': 'us-east-1', 'ZoneName': 'us-east-1b', 'ZoneId': 'use1-az1', 'GroupName': 'us-east-1', 'NetworkBorderGroup': 'us-east-1', 'ZoneType': 'availability-zone'}, {'State': 'available', 'OptInStatus': 'opt-in-not-required', 'Messages': [], 'RegionName': 'us-east-1', 'ZoneName': 'us-east-1c', 'ZoneId': 'use1-az2', 'GroupName': 'us-east-1', 'NetworkBorderGroup': 'us-east-1', 'ZoneType': 'availability-zone'}, {'State': 'available', 'OptInStatus': 'opt-in-not-required', 'Messages': [], 'RegionName': 'us-east-1', 'ZoneName': 'us-east-1d', 'ZoneId': 'use1-az4', 'GroupName': 'us-east-1', 'NetworkBorderGroup': 'us-east-1', 'ZoneType': 'availability-zone'}, {'State': 'available', 'OptInStatus': 'opt-in-not-required', 'Messages': [], 'RegionName': 'us-east-1', 'ZoneName': 'us-east-1e', 'ZoneId': 'use1-az3', 'GroupName': 'us-east-1', 'NetworkBorderGroup': 'us-east-1', 'ZoneType': 'availability-zone'}, {'State': 'available', 'OptInStatus': 'opt-in-not-required', 'Messages': [], 'RegionName': 'us-east-1', 'ZoneName': 'us-east-1f', 'ZoneId': 'use1-az5', 'GroupName': 'us-east-1', 'NetworkBorderGroup': 'us-east-1', 'ZoneType': 'availability-zone'}]

"""