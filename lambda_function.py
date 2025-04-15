import json
import requests
import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    # bucket = event[0][records][s3][key]
    print("Event Data --> ", event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    objKey = event['Records'][0]['s3']['object']['key']
    print(bucket, object)
    
    # Use boto3 to get the object from the bucket
    s3 = boto3.client('s3')
    print("Before Object")
    try:

        response = s3.get_object(Bucket=bucket, Key=objKey)
        # file_content = response['Body'].read().decode('utf-8')
        print("Before Read")
        file_content = response['Body'].read()
        print("After Read")
        # data = pd.read_csv(io.StringIO(file_content))
        data = pd.read_csv(io.BytesIO(file_content))
        print(data)
        print("After data")
        print("Hare Krishna!)
        # return bucket
    
        return{
            'statusCode': 200,
            'body': json.dumps('Excel file processed successfully!')
        }

    except Exception as e:
        print(f"Error processing file {e}")
        return{
            'statusCode': 500,
            'body': json.dumps(f'Error processing Excel file {e}')
        }