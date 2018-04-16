Role Name
=========

Role created for installing PHP 7 on AWS along with sub modules

Requirements
------------

Make sure to follow the steps in the main project creation

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

Apache needs to be restarted after PHP module has been successfully deployed on servers. This is done in the **handlers** folder of the roles directory. In the main playbook, we use *notify* module to send notification to the Apache to restart the service

Playbook script
----------------
Following is the playbook file for this role:

```yml
---
# tasks file for php
- name: Install PHP 7 with common packages
  yum: 
    name: "{{ item }}" 
    state: present
  with_items:
    - php70
    - php70-gd
    - php70-imap
    - php70-mbstring
    - php70-mysqlnd
    - php70-opcache
    - php70-pdo
    - php70-pecl-apcu
  notify: restart Apache
- name: Upload index.php to the destination
  copy:
    src: index.php
    dest: /var/www/html
    owner: ec2-user
    group: ec2-user

```

License
-------

BSD

Author Information
------------------
Gaurav Tripathi
