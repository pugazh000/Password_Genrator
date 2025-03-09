# **Cyberpunk Password Generator**

A **serverless password generator** that securely creates random passwords and stores them in **AWS DynamoDB**. The frontend is hosted on **AWS S3**, and the backend runs on **AWS Lambda (deployed using Zappa) with API Gateway**. 🚀

---

## **📌 Features**
✅ Generates strong passwords with custom length & character options  
✅ Stores passwords in **AWS DynamoDB**  
✅ Serverless deployment using **AWS Lambda & API Gateway**  
✅ Cyberpunk-themed UI hosted on **AWS S3**  
✅ Fully integrated frontend & backend  

---

## **🛠 Tech Stack**
- **Frontend:** HTML, CSS (Cyberpunk theme), JavaScript (Fetch API)
- **Backend:** Flask (Python), AWS Lambda (Serverless), API Gateway
- **Database:** AWS DynamoDB
- **Deployment Tools:** Zappa (for AWS Lambda), S3 (for hosting static files)

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/aws-password-generator.git
cd aws-password-generator
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### **3️⃣ Configure AWS Credentials**
Ensure you have **AWS CLI installed & configured**:
```sh
aws configure
```
📌 **Enter your:**
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `ap-southeast-1`)

---

## **🌐 AWS Deployment**

### **1️⃣ Deploy the Backend to AWS Lambda (Zappa)**
```sh
zappa init  # First-time setup
zappa deploy dev  # Deploy to AWS Lambda
```
✅ **After Deployment, note your API Gateway URL.**
Example: `https://your-api-id.execute-api.region.amazonaws.com/dev/generate`

### **2️⃣ Create a DynamoDB Table**
1. Go to **AWS DynamoDB Console**
2. Click **Create Table**
3. **Table Name:** `GeneratedPasswords`
4. **Primary Key:** `id` (String)
5. Click **Create**

### **3️⃣ Deploy the Frontend to AWS S3**
1. Go to **AWS S3 Console** → Create a new bucket
2. Enable **Static Website Hosting**
3. Upload `index.html`, `static/script.js`, and `static/style.css`
4. Make files **public** using this bucket policy:
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::your-bucket-name/*"
       }
     ]
   }
   ```

---

## **⚡ API Endpoints**
| Method | Endpoint | Description |
|--------|-------------|-------------|
| `GET` | `/generate` | Generates a random password |
| `GET` | `/passwords` | Retrieves stored passwords from DynamoDB |

---

## **💻 Usage**
1️⃣ Open **S3 Website URL**
2️⃣ Set your password preferences (length, symbols, numbers, uppercase)
3️⃣ Click **Generate Password**
4️⃣ Password is stored in **DynamoDB** & displayed on UI ✅

---

## **🔐 Security Considerations**
✅ **Do NOT expose AWS credentials in the code**  
✅ **Restrict API Gateway access** (Use IAM for security)  
✅ **Use HTTPS for secure communication**  

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **📞 Contact & Contributions**
Feel free to **fork** and contribute! Pull requests are welcome. 😊

