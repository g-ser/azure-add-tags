import os
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsPatchResource

credential = AzureCliCredential()
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

resource_client = ResourceManagementClient(credential, subscription_id)

# Update the list below with the resource id of each Azure resource where the tags need to be applied

resources=[
    f"/subscriptions/{subscription_id}/resourceGroups/demoGroup/providers/Microsoft.Storage/storageAccounts/myawesomestorageaccount3",
    f"/subscriptions/{subscription_id}/resourceGroups/DEMOGROUP/providers/Microsoft.Compute/virtualMachines/MYVM",
    f"/subscriptions/{subscription_id}/resourceGroups/DEMOGROUP/providers/Microsoft.Compute/disks/myVM_OsDisk_1_8a3e9415795543069735bb939bc475ac",
    f"/subscriptions/{subscription_id}/resourceGroups/demoGroup/providers/Microsoft.Network/networkSecurityGroups/myVMNSG",
    f"/subscriptions/{subscription_id}/resourceGroups/demoGroup/providers/Microsoft.Network/publicIPAddresses/myVMPublicIP",
    f"/subscriptions/{subscription_id}/resourceGroups/demoGroup/providers/Microsoft.Network/networkInterfaces/myVMVMNic",
    f"/subscriptions/{subscription_id}/resourceGroups/demoGroup/providers/Microsoft.Network/virtualNetworks/myVMVNET"
]

# Put in the dictionary below the tags that you want to add to the resources

tags = {
    "Dept": "Physics",
    "Status": "Normal"
}

tag_patch_resource = TagsPatchResource(
    operation="Merge",
    properties={'tags': tags}
)
# 
for resource in resources:
    resource_client.tags.begin_update_at_scope(resource, tag_patch_resource)
    print(f"Tags {tag_patch_resource.properties.tags} were added to existing tags on resource with ID: {resource}")
