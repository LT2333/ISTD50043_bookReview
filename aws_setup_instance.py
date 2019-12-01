import boto3
import pprint as pp
import os
from botocore.exceptions import ClientError

key = os.environ['AWS_KEY_LT']
secret_key = os.environ['AWS_SECRET_KEY_LT']
region_name = 'us-west-2'



#functions:

#Function for creating security group
def create_security_group(security_group_name):
    response = ec2_client.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '') #Get VPC id of this aws account

    try:
        response = ec2_client.create_security_group(GroupName=security_group_name,
                                             Description="Group7:This is for SUTD 50.0043 Big Data and Database project",
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
        pp.pprint('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

        data = ec2_client.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,      ## SSH
                 'ToPort': 22,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 27017,   ## MongoDB
                 'ToPort': 27017,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 3306,    ## mySQL
                 'ToPort': 3306,
                 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}

            ])
        pp.pprint('Ingress Successfully Set %s' % data)

    except ClientError as e:
        pp.pprint(e)

#Function for creating a key-pair for EC2 instance
def generate_key_pairs(key_name):  # Key_name needs to be unique *
    outfile = open('{}.pem'.format(key_name),'w')
    key_pair = ec2.create_key_pair(KeyName=key_name)
    KeyPairOut = str(key_pair.key_material)
    outfile.write(KeyPairOut)
    # print(KeyPairOut)
    print("Finish creating EC2 key paris")
    os.system("chmod 400 {}.pem".format(key_name))



# Connection
ec2 = boto3.resource('ec2', 
    aws_access_key_id=key,
    aws_secret_access_key=secret_key,
    region_name=region_name)
ec2_client = boto3.client('ec2',
    region_name=region_name,
    aws_access_key_id=key,
    aws_secret_access_key=secret_key)


#Check if our security group exists,otherwise create one
security_group_name='Group7_500043_ShelfRead'
try:
    response = ec2_client.describe_security_groups(GroupNames=[security_group_name])
    print("Security group: {} exits".format(security_group_name))
#     pp.pprint(response)
except ClientError as e:
#     pp.pprint(e)
    print("This security group doesn't exist,creating a new one...\n")
    create_security_group(security_group_name)


#Check if our key-pair exists,otherwise create one
key_name = "group7-bigdata-ec2-key"
key_not_exist = True

keyPairs = ec2_client.describe_key_pairs()
for key in keyPairs.get('KeyPairs'):
    if key.get('KeyName') == key_name:
        key_not_exist = False
        print("key-pair: {} exists.".format(key_name))
        break
if key_not_exist :
    print("Generating a unique key for EC2 instances")
    generate_key_pairs(key_name)


# Check elastic IP quota (We need at least 3 elastic ip address)
filters = [
    {'Name': 'domain', 'Values': ['vpc']}
]
addresses = ec2_client.describe_addresses(Filters=filters)
# print(addresses)
if len(addresses.get("Addresses"))> 5-3:
    print('\033[1m'+'\033[91m'+"This aws account will reach AddressLimit for elastic IPs (max 5) if it is a student account."+'\033[0m')
#     raise ValueError('This aws account will reach AddressLimit for elastic IPs (max 5) if it is a student account.')


# create 3 instances
instances = ec2.create_instances(
     ImageId='ami-06d51e91cea0dac8d',  #UBuntu 18.04LTS
     InstanceType='t2.micro',
     MinCount=1,
     MaxCount=3, # create 3 instances
     KeyName=key_name,
     SecurityGroups=[security_group_name,]
 )

# get instances' ID:
instance_ids = []
for instance in instances:
    print("Creating instance {} ...".format(instance.id))
    instance.wait_until_running()
    instance_ids.append(instance.id)
print(instance_ids)



# Allocate and associate elastic IP for each instance
ip_addr = {}
for instance_id in instance_ids:
    try:
        allocation = ec2_client.allocate_address(Domain='vpc')
        print("Generated elastic IP: "+allocation.get('PublicIp'))
        response = ec2_client.associate_address(AllocationId=allocation['AllocationId'],
                                         InstanceId=instance_id)
        print(response)
        ip_addr[instance_id] = allocation.get('PublicIp')
    except ClientError as e:
        print(e)
