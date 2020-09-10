APPLY A MACHINE LEARNING MODEL IN AZURE FUNCTIONS WITH PYTHON AND TENSORFLOW

This project uses Python, TensorFlow, and Azure Functions to deploy a machine learning model to classify images. 

The function will be created and deployed in local and in a Azure account using command lines and Visual Studio as well.

1) Prerequisites
    • Python 3.7.4 
	 python --version (Linux/MacOS) 
	 py --version (Windows) 

    • Azure Functions Core Tools
	To install Azure Functions Core Tools

	npm i -g azure-functions-core-tools@3 --unsafe-perm true –force

	Check version 
	func --version
    • Visual Studio Code

2) Create and activate a Python virtual environment
	Clone the project and in local navigate to the project folder and run the following commands 

	cd project
	py -m venv .venv ( to install python in virtual environment: sudo apt-get install python3-venv)
	.venv\scripts\activate

	To install python in virtual environment

	sudo apt-get install python3-venv

	To exit the virtual environment :
	 deactivate

3) Create a local functions project

    • Initialize a Python function app
	func init --worker-runtime python

    • Add a function named classify
	Make sure the folder project contains the required codes and files  to run the model and run the following command

	func new --name classify --template "HTTP trigger"

    • Open project/requirements.txt in a text editor and add the following dependencies required by the helper code and ave the file:
	tensorflow==1.14
	Pillow
	Requests

    • pip install --no-cache-dir -r requirements.txt

    • Run the function locally
	func start

    • Test the fonction locally
	In Posman, open the following URL to invoke the function with the URL of a cat image, insert an image under binary format and confirm that the returned 	JSON classifies the image as a cat.
	http://localhost:7071/api/classify
	
![Alt text](/Postman.png?raw=true "Test the Azure function with Postman")

4) Publish the function in Azure using Windows Power Shell

	Connect-AzAccount
	Get-AzRessource
	Get-AzContext

	Navigate to the folder « project », create a function in Azure

	az functionapp create --resource-group YOUR RESSOURCE GROUP  --os-type Linux --consumption-plan-location westeurope --runtime python --runtime-version 3.7 --functions-version 2 --name GIVE A NAME TO YOUR 		FUNCTION --storage-account YOUR STORAGE ACCOUNT

    • Publish the function from local to Azure

	func azure functionapp publish THE NAME OF THE FUNCTION IN AZURE

    • Create an API key for the function via Function Keys being founded in Azure
	The function has bean already deployed in Azure, to invoke it with Postman, enter the URL as the following :
	https://[THE NAME OF THE FUNCTION IN AZURE].azurewebsites.net/api/classify?code=[APIkey]
