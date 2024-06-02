import boto3


session = boto3.Session(
        aws_access_key_id='AKIA2UC3AJO7JSI5RENC',
    aws_secret_access_key='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',
    region_name='us-east-1'
    )

ec2 = session.client("ec2")

resp = ec2.describe_instances()
insta_map={}
for i in resp["Reservations"]:
    #print(i)
    for instance in i.get("Instances"):
        #print(instance)
        insta_map["InstanceId"]=instance.get("InstanceId")
        insta_map["InstanceName"]=instance.get("KeyName")
        insta_map["InstanceState"]=instance.get("State").get("Name")
        
print("instance info: ",insta_map)
insta_list = []
for i in insta_map:
    if i == "InstanceId":
        insta_list.append(insta_map.get("InstanceId"))

print(insta_list)

print("-------------------Starting Instances---------------------------------------------------------")
status = ec2.start_instances(InstanceIds=insta_list)
print(status)

print("-------------------Stopping Instances---------------------------------------------------------")
status = ec2.stop_instances(InstanceIds=insta_list)

print(status)




