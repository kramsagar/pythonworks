import boto3

# Creating a client with configuration
ec2 = boto3.client('ec2',aws_access_key_id='AKIA47CRYX73SLBEHN4G',
    aws_secret_access_key='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',
    region_name='us-east-1')

def get_ec2_instance_names():
    # Retrieve a list of EC2 instances
    response = ec2.describe_instances()

    # Extract and print the instance names
    instance_names = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            name = None
            # Find the Name tag if it exists
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break
            instance_names.append(name)

    return instance_names

if __name__ == "__main__":
    # Print the names of all EC2 instances
    names = get_ec2_instance_names()
    print("EC2 Instance Names:")
    for name in names:
        print(name)


"""
(.venv) PS D:\mydrive\DevopsWorks\PythonWork\Boto3> python .\Ec2Instance.py
EC2 Instance Names:
los
pgs
(.venv) PS D:\mydrive\DevopsWorks\PythonWork\Boto3>
"""