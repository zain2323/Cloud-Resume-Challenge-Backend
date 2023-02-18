#! /bin/bash
zip lambda_function.zip lambda_function.py
aws lambda update-function-code --function-name updateVisitorCount --zip-file fileb://lambda_function.zip
