import json

def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']
    message = event['message']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{last_name}, {first_name} {message} update",
        }),
    }
