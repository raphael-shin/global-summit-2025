# Gallery Backend

This project uses AWS CDK to construct the gallery backend infrastructure.

## Stacks

The project consists of the following stacks:

### 1. BYOC (Bring Your Own Container) Stacks
- Infrastructure for container management and deployment
- Key components:
  - FaceChain ECR Stack: Container registry for FaceChain model
  - FaceChain CodeBuild Stack: Build pipeline for FaceChain container
  - GFPGAN ECR Stack: Container registry for GFPGAN model
  - GFPGAN CodeBuild Stack: Build pipeline for GFPGAN container

### 2. FaceChain Stacks
- Infrastructure for FaceChain model deployment and management
- Key components:
  - SageMaker Endpoint Stack: Model deployment endpoint
  - CodeBuild Trigger Stack: Automated build triggers
  - CodeBuild Status Checker Stack: Build status monitoring

### 3. GFPGAN Stacks
- Infrastructure for GFPGAN model deployment and management
- Key components:
  - SageMaker Endpoint Stack: Model deployment endpoint
  - CodeBuild Trigger Stack: Automated build triggers
  - CodeBuild Status Checker Stack: Build status monitoring

### 4. API Gateway Stacks
- REST API endpoint management and configuration
- Key components:
  - Image Upload API (/apis/images/upload)
  - Image Retrieval API (/apis/images/{userId})
  - User Agreement API (/agree)
  - CORS configuration and permission management
  - Lambda integration

### 5. Cognito Stacks
- User authentication and authorization management
- Key components:
  - User Pool configuration
  - Client application settings
  - Domain configuration

### 6. DynamoDB Stacks
- Data storage management
- Key tables:
  - Process Table: Image processing status management
  - Display Table: Image display information management
  - Display History Table: Image display history tracking
  - Base Resource Table: Base resource information storage
  - User Agreement Table: User consent information management

### 7. Lambda Stacks
- Serverless function management
- Key functions:
  - Image Processing Lambdas:
    - Face Crop Lambda: Face image cropping processing
    - Face Swap Lambda: Face swapping processing
    - Face Swap Completion Lambda: Face swap completion handling
  - S3 event-based automated processing configuration

### 8. S3 Stacks
- Object storage management
- Key features:
  - Image storage configuration
  - CORS settings
  - Bucket policy management
  - Event notification setup

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## How to deploy

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

Enjoy!
