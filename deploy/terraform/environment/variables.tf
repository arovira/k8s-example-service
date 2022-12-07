############################# Generic Vars #############################
variable "app" {
  type    = string
  default = "fastapi-k8s-example-app"
}
variable "aws_region" {
  type        = string
  description = "AWS region to create resources"
}
variable "aws_profile" {
  type        = string
  description = "AWS profile to authenticate"
}
