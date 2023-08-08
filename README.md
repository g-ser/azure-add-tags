## About the current Repository

This repository includes a simple script for applying tags to Azure resources using Python. It uses the ```Merge``` operation which adds tags to a resource that already has tags (i.e. it keeps the tags which are already applied to the resource). The contents of this repository is a subset of the article [Apply tags with Python](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-python) from Azure documentation. 

## Prerequisites<a name="prerequisites"></a>

* Python 3.7 or later installed

* Since authentication happens using the ```AzureCliCredential``` class, from ```azure.identity``` python package, you need to run ```az login``` first on the same terminal which will eventually used to run the python script 

* An environment variable which holds the Azure Subscription ID:
   ```Bash
   export AZURE_SUBSCRIPTION_ID=your-subscription-id
   ```
* It is recommended to create a Python virtual environment to install the needed dependencies of the next step and run the script. Check this YouTube video about making a python virtual environment in vscode: [Setup A Virtual Environment For Python In Visual Studio Code](https://youtu.be/GZbeL5AcTgw)

* Install the required packages listed in [requirements.txt](./requirements.txt) file:
   ```Bash
   pip install -r requirements.txt
   ```

* You need to specify the tags that you want to add to the resources in the [add-tags.py](./add-tags.py) python script

* You need to prepare the list of the IDs of the Azure resources where the tags will be added and specify them in the [add-tags.py](./add-tags.py) python script

## Run the script

Open a command prompt that has Python in its path, use ```az login``` to log into Azure and set the environment variable ```AZURE_SUBSCRIPTION_ID``` as described in [Prerequisites](#prerequisites) and finally run the script:

```Bash
python add-tags.py
```