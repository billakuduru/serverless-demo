import json
import os
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def create_order(event, context):
    body = json.loads(event.get('body', '{}'))
    order_id = str(uuid.uuid4())
    item = {
        'id': order_id,
        'customer': body.get('customer', 'anonymous'),
        'item': body.get('item', 'unknown'),
        'status': 'created'
    }
    table.put_item(Item=item)
    return {
        'statusCode': 201,
        'body': json.dumps({'order_id': order_id})
    }

def get_order(event, context):
    order_id = event['pathParameters']['id']
    resp = table.get_item(Key={'id': order_id})
    if 'Item' in resp:
        return {
            'statusCode': 200,
            'body': json.dumps(resp['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Order not found'})
        }
