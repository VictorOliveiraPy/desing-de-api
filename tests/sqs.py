
{
  "Version": "2008-10-17",
  "Id": "only_production_accounts",
  "Statement": [
    {
      "Sid": "deny_organization_test_accounts",
      "Effect": "Deny",
      "Principal": {
        "AWS": [
          "arn:aws:iam::579982983588:root",
          "arn:aws:iam::678697092296:root"
        ]
      },
      "Action": [
        "sqs:SendMessage",
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:PurgeQueue",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "arn:aws:sqs:us-east-1:412729474065:seller_tasks_submit_ten_products__seller__create"
    },
    {
      "Sid": "allow_organization_accounts",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": [
        "sqs:SendMessage",
        "sqs:ReceiveMessage",
        "sqs:DeleteMessage",
        "sqs:PurgeQueue",
        "sqs:GetQueueAttributes"
      ],
      "Resource": "arn:aws:sqs:us-east-1:412729474065:seller_tasks_submit_ten_products__seller__create",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-9z55eim1qz"
        }
      }
    },
    {
      "Sid": "topic-subscription-arn:aws:sns:us-east-1:412729474065:seller__created",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:us-east-1:412729474065:seller_tasks_submit_ten_products__seller__create",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:sns:us-east-1:412729474065:seller_tasks_submit_ten_products__seller__create"
        }
      }
    }
  ]
}
