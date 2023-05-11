import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { S3 } from 'aws-cdk-lib/aws-ses-actions';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications';
import { Construct } from 'constructs';
import * as dotenv from 'dotenv';

// load env variables
dotenv.config();

export class ThumbingServerlessCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const bucketName: string = process.env.THUMBING_BUCKET_NAME as string;
    const folderInput: string = process.env.THUMBING_S3_FOLDER_INPUT as string;
    const folderOutput: string = process.env.THUMBING_S3_FOLDER_OUTPUT as string;
    const webhookUrl: string = process.env.THUMBING_WEBHOOK_URL as string;
    const topicName: string = process.env.THUMBING_TOPIC_NAME as string;
    const functionPath: string = process.env.THUMBING_FUNCTION_PATH as string;
    console.log('bucketName',bucketName)
    console.log('folderInput',folderInput)
    console.log('folderOutput',folderOutput)
    console.log('webhookUrl',webhookUrl)
    console.log('topicName',topicName)
    console.log('functionPath',functionPath)

    //const bucket = this.createBucket(bucketName);
    const bucket = this.importBucket(bucketName);
    const lambda = this.createLambda(functionPath, bucketName, folderInput, folderOutput);

    this.createS3NotifyToLambda(folderInput,lambda,bucket)

    const s3ReadWritePolicy = this.createPolicyBucketAccess(bucket.bucketArn)
    lambda.addToRolePolicy(s3ReadWritePolicy);
  }

   

    createBucket(bucketName: string): s3.IBucket {
      const bucket = new s3.Bucket(this, 'AssetsBucket', {
        bucketName: bucketName,
        removalPolicy: cdk.RemovalPolicy.DESTROY,
      });
      return bucket;
    }

    importBucket(bucketName: string): s3.IBucket {
      const bucket = s3.Bucket.fromBucketName(this, "AssetsBucket", bucketName);
      return bucket;
    }

    createLambda(functionPath: string, bucketName: string, folderInput: string, folderOutput: string): lambda.IFunction {
      const lambdaFunction = new lambda.Function(this, 'ThumbLambda', {
        runtime: lambda.Runtime.NODEJS_18_X,
        handler: 'index.handler',
        code: lambda.Code.fromAsset(functionPath),
        environment: {
          DEST_BUCKET_NAME: bucketName,
          FOLDER_INPUT: folderInput,
          FOLDER_OUTPUT: folderOutput,
          PROCESS_WIDTH: '512', //image size in pixels
          PROCESS_HEIGHT: '512'
        }
      })
      return lambdaFunction;
    }

    createS3NotifyToLambda(prefix: string, lambda: lambda.IFunction, bucket: s3.IBucket): void {
      const destination = new s3n.LambdaDestination(lambda);
        bucket.addEventNotification(
        s3.EventType.OBJECT_CREATED_PUT,
        destination,
        {prefix: prefix} // folder to contain the original images
      )
    }

    createPolicyBucketAccess(bucketArn: string){
      const s3ReadWritePolicy = new iam.PolicyStatement({
        actions: [
          's3:GetObject',
          's3:PutObject',
        ],
        resources: [
          `${bucketArn}/*`,
        ]
      });
      return s3ReadWritePolicy;
    }
    
  
}
