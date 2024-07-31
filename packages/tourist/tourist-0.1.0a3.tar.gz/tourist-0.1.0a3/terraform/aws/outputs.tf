
output "api_endpoint" {
  description = "Base url for api"
  value       = aws_apigatewayv2_api.api.api_endpoint
}
