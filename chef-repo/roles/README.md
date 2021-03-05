Create roles here, in either the Role Ruby DSL (.rb) or JSON (.json) files. To install roles on the server, use knife.

We expect any node we create to have a single role as an entry point. All roles other than `base` will include `base`
as the first entry in their run_list. 

For more information on roles, see the Chef docs site:

https://docs.chef.io/roles.html
