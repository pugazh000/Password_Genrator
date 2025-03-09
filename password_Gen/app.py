from flask import Flask, jsonify
import boto3
import random
import string

app = Flask(__name__)

dynamodb = boto3.resource("dynamodb", region_name="ap-southeast-1")
table = dynamodb.Table("GeneratedPasswords")

@app.route("/generate", methods=["GET"])
def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    
    table.put_item(Item={"id": str(random.randint(1000, 9999)), "password": password})
    
    return jsonify({"password": password})

@app.route("/passwords", methods=["GET"])
def list_passwords():
    response = table.scan()
    passwords = [item["password"] for item in response.get("Items", [])]
    return jsonify({"generated_passwords": passwords})

if __name__ == "__main__":
    app.run(debug=True)
