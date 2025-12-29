
import boto3
import json

s3 = boto3.client('s3')
bedrock = boto3.client('bedrock-runtime')  # <- important AWS documentation

def handler(event, context):
    bucket_name = 'aws-bedrock-docs-unique'
    file_key = 'sample.txt'
    
    s3_object = s3.get_object(Bucket=bucket_name, Key=file_key)
    text = s3_object['Body'].read().decode('utf-8')
    
    prompt = event.get('question', f"Summarize the document:\n{text}")
    
    response = bedrock.invoke_model(
        modelId='amazon.titan-tg1-large',
        contentType='application/json',
        body=json.dumps({"inputText": prompt})
    )
    
    result = response['body'].read().decode('utf-8')
    
    return {
        "statusCode": 200,
        "body": result
    }
