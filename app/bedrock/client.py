import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)


def invoke_model(body, model="amazon.nova-micro-v1:0"):

    response = bedrock.invoke_model(
        modelId=model,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json"
    )

    return json.loads(response["body"].read())