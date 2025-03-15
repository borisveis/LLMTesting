resource "aws_codebuild_project" "LLMTesting" {
  name         = "LLMTesting"
  description  = "LLMTesting CodeBuild project"
  service_role = "arn:aws:iam::211125687103:role/service-role/codebuild-codebuildlearning-service-role"

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/standard:5.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"
  }

  source {
    type            = "GITHUB"
    location        = "https://github.com/borisveis/LLMTesting.git"
    git_clone_depth = 1
  }
}

resource "aws_iam_role" "codebuild" {
  name = "example-codebuild-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "codebuild.amazonaws.com"
        }
      }
    ]
  })
}
