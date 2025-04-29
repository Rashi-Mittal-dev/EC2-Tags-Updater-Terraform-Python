provider "aws" {
  region = "us-east-1" # ✅ Change this to match your AWS Console region
}

variable "instances" {
  type = map(object({
    department = string
  }))
  default = {
    webserver01       = { department = "Backend" }
    webserver02       = { department = "Frontend" }
    database04        = { department = "QA" }
    ansible           = { department = "Devops" }
    scanner           = { department = "" }
    activedirectory02 = { department = "ITOps" }
    database03        = { department = "Frontend" }
    jenkins           = { department = "" }
  }
}

resource "aws_instance" "multi" {
  for_each      = var.instances
  ami           = "ami-0c02fb55956c7d316" # ✅ Make sure it's valid for your region
  instance_type = "t2.micro"

  tags = {
    Name       = each.key
    Department = each.value.department
    Hostname   = each.key 
  }
}
