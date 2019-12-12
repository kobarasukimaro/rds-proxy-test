This repository is for trying out the AWS RDX Proxy.

## Required Software
- [Node.js >= 6](https://nodejs.org/)
- [Python 3.7](https://www.python.org/)
- [serverless framework](https://serverless.com/)

## Convenient
- [awscli](https://aws.amazon.com/cli/)

## Build
### CloudFormation
#### Create Configuration File
```
$ cd cfn
$ cp parameter.json.sample parameter.json
```

#### Execute Command
```
$ cd cfn
$ STACKNAME=proxy-test-stack && AWS_PROFILE=xxx && REGION=xxx && \
aws cloudformation create-stack --stack-name $STACKNAME  \                           
--template-body file://rds-proxy-sample.yml \
--cli-input-json file://parameter.json --profile $AWS_PROFILE --region $REGION
```

#### Created from the Management Console

### Serverless Framework
#### Create Configuration File
```
$ cd sls/conf
$ cp stage_name.yml.sample xxx.yml
```

#### Deploy
```
$ cd sls
$ sls deploy --stage xxx -r xxx
```

### Create RDS Proxy
[Created from the Management Console](https://aws.amazon.com/jp/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/)