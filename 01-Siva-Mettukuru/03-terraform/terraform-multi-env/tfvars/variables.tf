variable "instance_names" {
    type = map
    # default = {
    #     db-dev= "t3.small"
    #     backend-dev = "t3.micro"
    #     frontend-dev = "t3.micro"
    # }
}

variable "environment" {
   # default = "dev"
}

variable "common_tags" {
    type = map
    default = {
        Project = "Expense"
        Terraform = "true"
    }
}

variable "domain_name" {
    default = "shahulahmed.online"
}

variable "zone_id" {
    default = "Z04446051G6JOTCFJY5K3"
}