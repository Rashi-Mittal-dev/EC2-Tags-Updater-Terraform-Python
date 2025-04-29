
# 🐍 AWS EC2 Tag Updater – Python Script

## 🧩 Task Overview

An organization has multiple EC2 instances in AWS with tags like `Hostname` and `Department`. They requested to update the `Department` tag for specific instances based on a CSV file that includes:

- `Hostname`
- `Current Department`
- `New Department`

This script automates the update using the AWS Boto3 SDK.

---

## 📁 Input CSV Format

**Filename:** `update_tags.csv`

| Hostname         | CurrentDepartment | NewDepartment |
|------------------|-------------------|---------------|
| webserver01      | Backend           | Frontend      |
| webserver02      | Frontend          | Frontend      |
| database04       | QA                | Backend       |
| ansible          | Devops            | Backend       |
| scanner          | <no-value>        | Devops        |
| activedirectory02| ITops             | ITops         |
| database03       | Frontend          | Backend       |
| jenkins          | <no-value>        | Devops        |

---

## 📜 Script Description

The script uses Boto3 to:

- Search for EC2 instances based on the `Hostname` tag.
- Compare the current `Department` tag with the provided `CurrentDepartment`.
- Skip mismatches and log them.
- Update the `Department` tag if matching or if no current value exists.

---

## 🚀 Usage Instructions

1. Install Boto3 if not already installed:

pip install boto3


2. Configure AWS credentials using AWS CLI:

aws configure


3. Save the CSV file as `update_tags.csv` in the script's directory.

4. Run the script:

python updateScript.py


---

## 🔐 IAM Permissions Required

Ensure the IAM user or role has these EC2 permissions:

- `ec2:DescribeInstances`
- `ec2:CreateTags`

---

## 🧪 Output Example

🚀 Starting Department tag update process...

🔍 Processing Hostname: webserver01
✅ Updated i-0e896c232a6fc9e2b — Department → Frontend
🔍 Processing Hostname: webserver02
✅ Updated i-0fae4077d6e7753a4 — Department → Frontend
🔍 Processing Hostname: database04
✅ Updated i-0bef440667559682b — Department → Backend
🔍 Processing Hostname: ansible
✅ Updated i-097dcfe631d6431b4 — Department → Backend
🔍 Processing Hostname: scanner
✅ Updated i-0c6b3dd699877b007 — Department → Devops
🔍 Processing Hostname: activedirectory02
✅ Updated i-029668b2ec6e55d75 — Department → ITops
🔍 Processing Hostname: database03
✅ Updated i-048caf6332462f392 — Department → Backend
🔍 Processing Hostname: jenkins
✅ Updated i-0e2f37cb9abc757c2 — Department → Devops

📊 Summary Report
✔️ Updated: 8
❌ Failed: 0
❓ Not Found: 0
✅ Tag update process completed.

---

## 📦 Files Included

- `updateScript.py` – Python script for EC2 tag updates
- `update_tags.csv` – Sample input file
- `README.md` – Task documentation
- `TASK3.pdf` – Documentation in PDF format

---


