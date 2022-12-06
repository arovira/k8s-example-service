module "ecr_repo" {
  source                                       = "git::git@github.com:arovira/tfm-aws-ecr-repository.git"
  ecr_name                                     = var.app
  enable_access_from_external_account_clusters = false
}

output "repository_url" {
  value = module.ecr_repo.repository_url
}
