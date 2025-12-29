# AWS Bedrock Internal Assistant Demo

## Overview
This project demonstrates a simple internal AI assistant using AWS Lambda, S3, and Amazon Bedrock. The Lambda function reads a document from S3 and responds to user questions using a Bedrock model.

## Features
- AWS Lambda integration
- S3 bucket document reading
- Amazon Bedrock AI Q&A
- Event-driven testing via Lambda console

## How to Use
1. Upload a text file to S3.
2. Deploy the Lambda function with the appropriate IAM role.
3. Test via Lambda console by sending a JSON event with a `question`.

## Example Test Event
```json
{
  "question": "What is the main topic of the document?"
}

## Example Result
```json
{
  "statusCode": 200,
  "body": "{\"inputTextTokenCount\":9,\"results\":[{\"tokenCount\":20,\"outputText\":\"\\nThe main topic of the document is the history of the development of the English language.\\n\",\"completionReason\":\"FINISH\"}]}"
}

## Notes
1. Make sure the Lambda function has the proper IAM role with access to S3 and Bedrock.
2. The S3 bucket and Lambda must be in the same AWS region.

