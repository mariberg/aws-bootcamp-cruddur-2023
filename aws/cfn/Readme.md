## Architecture Guide

Before you run any templates, be sure to create an S3 bucket to contain all of the artifacts for CloudFormation.

```
aws s3 mk s3://cfn-artifacts
export CFN_BUCKET="cloudproject-cfn-artifacts"
gp env CFN_BUCKET="cloudproject-cfn-artifacts"
```