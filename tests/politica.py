{
  "Version": "2008-10-17",
  "Id": "__default_policy_ID",
  "Statement": [
    {
      "Sid": "__owner_statement",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::412729474065:root"
      },
      "Action": "SQS:*",
      "Resource": "arn:aws:sqs:us-east-1:412729474065:product_tasks__seller_products__created"
    },
    {
      "Sid": "topic-subscription-arn:aws:sns:sa-east-1:412729474065:seller_product__created",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:us-east-1:412729474065:product_tasks__seller_products__created",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:sns:sa-east-1:412729474065:seller_product__created"
        }
      }
    },
    {
      "Sid": "topic-subscription-arn:aws:sns:us-east-1:412729474065:seller_product__created",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:us-east-1:412729474065:product_tasks__seller_products__created",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:sns:us-east-1:412729474065:seller_product__created"
        }
      }
    }
  ]
}