import boto3
import csv

# Initialize EC2 client using default AWS CLI config
ec2 = boto3.client('ec2')

def update_department_tags(csv_file):
    print("🚀 Starting Department tag update process...\n")

    updated = 0
    not_found = 0
    failed = 0

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hostname = row['Hostname'].strip()
            new_dept = row['NewDepartment'].strip()

            print(f"🔍 Processing Hostname: {hostname}")

            try:
                # Find instances with matching Hostname tag
                response = ec2.describe_instances(
                    Filters=[
                        {'Name': 'tag:Hostname', 'Values': [hostname]},
                        {'Name': 'instance-state-name', 'Values': ['running']}
                    ]
                )

                matched_instances = [
                    instance
                    for reservation in response['Reservations']
                    for instance in reservation['Instances']
                ]

                if not matched_instances:
                    print(f"⚠️ No EC2 instances found with Hostname: {hostname}")
                    not_found += 1
                    continue

                for instance in matched_instances:
                    instance_id = instance['InstanceId']
                    try:
                        ec2.create_tags(
                            Resources=[instance_id],
                            Tags=[{'Key': 'Department', 'Value': new_dept}]
                        )
                        print(f"✅ Updated {instance_id} — Department → {new_dept}")
                        updated += 1
                    except Exception as e:
                        print(f"❌ Failed to update {instance_id}: {str(e)}")
                        failed += 1

            except Exception as e:
                print(f"❌ Error fetching instances for Hostname {hostname}: {str(e)}")
                failed += 1

    print("\n📊 Summary Report")
    print(f"✔️ Updated: {updated}")
    print(f"❌ Failed: {failed}")
    print(f"❓ Not Found: {not_found}")
    print("✅ Tag update process completed.")

# Example usage
update_department_tags('update_tags.csv')
