import boto3
import json

s3 = boto3.client('s3')
bedrock = boto3.client('bedrock')

def handler(event, context):
    bucket_name = 'aws-bedrock-docs-unique'
    file_key = 'sample.txt'
    
    s3_object = s3.get_object(Bucket=bucket_name, Key=file_key)
    text = s3_object['Body'].read().decode('utf-8')
    
    response = bedrock.invoke_model(
        ModelId='amazon.titan-tg1-large',
        ContentType='application/json',
        Body=json.dumps({"input_text": text})
    )
    
    result = response['Body'].read().decode('utf-8')
    
    return {
        "statusCode": 200,
        "body": result
    }
