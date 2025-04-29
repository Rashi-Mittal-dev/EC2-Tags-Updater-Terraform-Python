variable "instance_details" {
  description = "List of EC2 instances with hostname and department"
  type = list(object({
    hostname   = string
    department = string
  }))
}
