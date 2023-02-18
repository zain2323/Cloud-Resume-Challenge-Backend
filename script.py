import json
import boto3

dynamodb =  boto3.resource('dynamodb')
table = dynamodb.Table('Visitors')

def read():
    return table.get_item(
        Key={
            "id": 0
        }
    )['Item']["counts"]

def update(val):
    response = table.update_item(
            Key={
                'id': 0,
            },
            UpdateExpression='SET counts = :newval',
            ExpressionAttributeValues={
                ':newval': val
            }
        )
    return response["ResponseMetadata"]["HTTPStatusCode"]



def increment_counter():
    prev = read()
    status = update(prev+1)
    if status == 200:
        return read()
    else:
       return -1
        
def lambda_handler(event, context):
    # TODO implement
    val = increment_counter()
    response = {
        "count": str(val)

    }
    return {
        'statusCode': 200,
        'headers': {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        "body": json.dumps(response)
    }
