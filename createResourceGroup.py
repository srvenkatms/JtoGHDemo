import os
import subprocess

resource_group_name = "myResourceGroup1"
location = "EastUS"  # Update the region as per your requirement

def login_to_azure():
    # Login to Azure using a service principal
    subprocess.run([
        "az", "login", "--service-principal",
        "-u", os.getenv("AZURE_CLIENT_ID"),
        "-p", os.getenv("AZURE_CLIENT_SECRET"),
        "--tenant", os.getenv("AZURE_TENANT_ID")
    ], check=True)

def create_resource_group():
    # Create the resource group using Azure CLI
    subprocess.run([
        "az", "group", "create",
        "--name", resource_group_name,
        "--location", location
    ], check=True)

def verify_resource_group_creation():
    # Verify if the resource group was created successfully
    subprocess.run([
        "az", "group", "show",
        "--name", resource_group_name
    ], check=True)

if __name__ == "__main__":
    login_to_azure()
    create_resource_group()
    verify_resource_group_creation()
