import boto3

ec2 = boto3.resource('ec2')


import boto3
import botocore
import paramiko

ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
     ImageId='ami-04b9e92b5572fa0d1',
     MinCount=1,
     MaxCount=3, # create 3 instances
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )





def execute_commands_on_linux_instances(client, commands, instance_ids):
    """Runs commands on remote linux instances
    :param client: a boto/boto3 ssm client
    :param commands: a list of strings, each one a command to execute on the instances
    :param instance_ids: a list of instance_id strings, of the instances on which to execute the command
    :return: the response from the send_command function (check the boto3 docs for ssm client.send_command() )
    """

    resp = client.send_command(
        DocumentName="AWS-RunShellScript", # One of AWS' preconfigured documents
        Parameters={'commands': commands},
        InstanceIds=instance_ids,
    )
    return resp

# Example use:
ec2_client = boto3.client('ec2') # Need your credentials here
commands = ['echo "hello world"']
instance_ids = ['an_instance_id_string']
execute_commands_on_linux_instances(ec2_client, commands, instance_ids)
