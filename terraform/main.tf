terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.64.0"
    }
  }

  backend "s3" {
    bucket         = "cathycodes-terraform-state"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}

provider "aws" {
  region = var.region

  default_tags {
    tags = {
      Owner       = var.owner
      Project     = var.project_name
      Environment = var.environment
    }
  }
}

resource "aws_s3_bucket" "project_resources" {
  bucket = local.repo_bucket
}