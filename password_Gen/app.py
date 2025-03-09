import boto3
import random
import string
from flask import Flask, jsonify

app = Flask(__name__)

# AWS DynamoDB setup
dynamodb = boto3.resource("dynamodb", region_name="ap-southeast-1")
table_name = "GeneratedPasswords"

# Create the table (Run once manually)
try:
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    table.wait_until_exists()
except:
    table = dynamodb.Table(table_name)

@app.route("/generate", methods=["GET"])
def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))

    # Store password in DynamoDB
    table.put_item(Item={"id": str(random.randint(1000, 9999)), "password": password})

    return jsonify({"password": password})

@app.route("/passwords", methods=["GET"])
def list_passwords():
    response = table.scan()
    passwords = [item["password"] for item in response.get("Items", [])]
    return jsonify({"generated_passwords": passwords})

if __name__ == "__main__":
    app.run()
