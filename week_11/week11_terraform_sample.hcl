# Terraform provisions infrastructure from code using declarative configuration files. 

provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "web" {
  ami = "ami-123456"
  instance_type = "t2.micro"
}
