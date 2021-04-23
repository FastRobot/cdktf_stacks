# Terraform described infrastructure

This directory contains two intertwined terraform projects:

* `modules/` Collections of reusable infrastructure modules, written in HCL
* `live/` Managed via terragrunt, the desired current state of the managed cloud resources

### `live/` structure
This folder structure allows for the leaf directories to act as root terraform modules/workspaces. The `terragrunt.hcl` file contain pointers to terraform modules plus some input variables, along with a mechanism for depending on the output of another independent workspace. The `terragrunt` utility can gather all the dependencies and generate a temporary directory in which to run terraform. 

CI handles most of this, so your git interactions with this `live/` directory result in changes to copies of infrastructure described in `modules/`. 
By creating a `terragrunt.hcl` file at the leaf of the `<account>/<region>/<environment>/<stack>/` structure, you can inherit information common to those accounts/regions and reduce the amount of config needed to invoke those resources. The structure is better described below:

```
.
├── non-prod - Generally this maps to an account. 
│   ├── account.hcl - contains the name and account id
│   └── us-west-2 - what region the stack lives in, regionless (eg IAM) in _global
│       ├── region.hcl - a place to put region-specifc variables
│       └── stage - some arbitrary name for this group of stacks. 
│           ├── env.hcl - you could vary size or number across a set of stacks with one edit here
│           └── monitoring - descriptive name of some invocation of a tf module
│               └── terragrunt.hcl - the file which names a version of a module and processes variables into a single set of inputs to this module
└── terragrunt.hcl

```
  

## Github Action driven
The two workflows `pull_request_terragrunt.yml` and `push_to_environment_terraform.yaml` will

### On Pull request
* ensure any commits to this directory or below pass basic validation and formatting checks
* run a `terraform plan` against the cloud APIs
* append the "what would I change if you merged me" output to the PR

## Development