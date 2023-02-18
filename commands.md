## To update the lambda function
```
aws lambda update-function-code --function-name updateVisitorCount --zip-file fileb://updateVisitorCounter.zip
```

## To retrieve ARN of a role
```
aws iam get-role --role-name <rolename>
```