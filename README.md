# 🚀 Serverless Demo

A fully automated demo showcasing how to deploy a **serverless AWS Lambda application** backed by a **DynamoDB table** using **Terraform for infrastructure** and **Serverless Framework for the application**, with **Azure DevOps Pipelines** for CI/CD.

---

## ✨ Features

✅ **Infrastructure as Code with Terraform**  
✅ **Serverless Framework Lambda Functions**  
✅ **HTTP API Gateway Endpoints**  
✅ **CI/CD with Azure Pipelines**

---

## ⚙️ Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform/install) >= 1.3.0  
- [Serverless Framework](https://www.serverless.com/framework/docs/getting-started) (v4)  
- [Python 3.11](https://www.python.org/downloads/)  
- AWS CLI configured (`aws configure`)

---

## 🚀 Deployment (via Azure Pipelines)

The pipeline is defined in [`azure-pipelines.yml`](./azure-pipelines.yml).  
On every push to `main`:

1. **Terraform Apply**  
   Initializes and applies Terraform in `infra/`.

2. **Capture Outputs**  
   Fetches DynamoDB table name and IAM role ARN from Terraform outputs.

3. **Serverless Deploy**  
   Deploys Lambda functions with the captured environment variables.


## 🌐 API Endpoints

After deployment, Serverless will output a base URL. Use it like this:

### Create Order & Get order

curl -X POST https://<api-url>/order \
  -H "Content-Type: application/json" \
  -d '{"customer": "test", "item": "demo"}

curl https://<api-url>/order/<order_id>