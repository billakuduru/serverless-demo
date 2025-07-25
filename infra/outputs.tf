output "lambda_role_arn" {
  value = aws_iam_role.lambda_exec.arn
}

output "table_name" {
  value = aws_dynamodb_table.demo_table.name
}
