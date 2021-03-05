# Data Bags

This directory contains directories of the various data bags you create for your infrastructure. Each subdirectory corresponds to a data bag on the Chef Infra Server, and contains JSON files of the items that go in the bag.

In this directory, you'll find an users data bag directory called `users`, which contains an item definition
named for each user being managed.

For more information on data bags, see the Chef docs site:

https://docs.chef.io/data_bags.html

# Encrypted Data Bags

We intend to leverage KMS or SSM to distribute secrets to nodes, but if we wanted to,
we could switch to encrypted data bags and only use KMS or SSM Parameter Store to share the
unlock secret.

Encrypted data bags allow you to encrypt the contents of your data bags. The content of attributes will no longer be searchable. To use encrypted data bags, first you must have or create a secret key.

    openssl rand -base64 512 > secret_key

You may use this secret_key to add items to a data bag during a create.

    knife data bag create --secret-file secret_key passwords mysql

You may also use it when adding ITEMs from files,

    knife data bag create passwords
    knife data bag from file passwords data_bags/passwords/mysql.json --secret-file secret_key

The JSON for the ITEM must contain a key named "id" with a value equal to "ITEM" and the contents will be encrypted when uploaded. For example,

    {
      "id": "mysql",
      "password": "abc123"
    }

Without the secret_key, the contents are encrypted.

    knife data bag show passwords mysql
    id:        mysql
    password:  2I0XUUve1TXEojEyeGsjhw==

Use the secret_key to view the contents.

    knife data bag show passwords mysql --secret-file secret_key
    id:        mysql
    password:  abc123


For more information on encrypted data bags, see the Chef docs site:

https://docs.chef.io/data_bags.html
