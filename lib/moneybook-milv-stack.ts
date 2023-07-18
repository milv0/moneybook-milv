import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { S3BaseStack } from './s3-stack';
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class MoneybookMilvStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    new S3BaseStack(this, 's3Stack', props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'MoneybookMilvQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
  }
}
