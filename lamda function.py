import json
from time import sleep
from json import dumps
import random
import boto3

def lambda_handler(event, context):
    client = boto3.client('kinesis')
    payload_part=json.loads(event['body'])['payload']
    for i in payload_part:
        light_illumination=i['values']['lux']
        capture_time=i['time']
        data={"light_illumination":light_illumination,"capture_time":capture_time}
        print(data)
        client.put_record(
            StreamName="DataLogger",
            Data=json.dumps(data),
            PartitionKey="1"
        )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
