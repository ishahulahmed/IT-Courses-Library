variable "ami_id" {
    type = string
    default = "ami-090252cbe067a9e58"
  
}

variable "security_group_ids" {
    type = list
    default = ["sg-02f9724521364723a"] # replace with your SG ID.
}

variable "instance_type" {
  default = "t2.micro"
  type = string
}

variable "tags" {
    type = map
    default = {} # this means empty, so not mandatory
}