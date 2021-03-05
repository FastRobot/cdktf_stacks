# Overview of the embedded chef-repo

The contents of this directory will be vetted and pushed to s3 for any commits
that end up on the "magic" persisted branch names, currently `main` and `staging`

This is the place where cookbooks, roles, environments, data bags and other artifacts for managing systems with Chef will live.

# Repository Directories

This repository contains several directories, and each directory contains a README file that describes what it is for in greater detail, and how to use it for managing your systems with Chef.

- `cookbooks/` - Cookbooks you download or create.
- `data_bags/` - Store data bags and items in .json in the repository.
- `roles/` - Store roles in .rb or .json in the repository.
- `environments/` - Store environments in .rb or .json in the repository.

# Configuration

This repo does not interact with a chef server, instead we attempt to bundle the 
entire repo into a tarball which is put on s3 and synced to clients on demand.

# Testing

Github Actions should take some steps to vet this repo prior to pushing, but in general, each 
cookbook in the cookbooks/ repo should have a `rspec` and `test-kitchen` test suite, along with passing `cookstyle`

