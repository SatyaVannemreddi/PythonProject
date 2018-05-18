import boto3

if _name__ == '--main--':
    session = boto3.Session(profile_name='satya')
    ec2 = session.resource("ec2")
    for i in ec2.instances.all():
        print(i)
