Role: Apache
=========

This role has been created to install the apache (httpd) webserver on the AWS cloud.

Requirements
------------

It is imperative that we remove the httpd (apache) service during the inital checks. The PHP role by default has httpd24 apache webserver installed when setting up the role for PHP.

Description
--------------
We are first checking here to see if httpd24 apache webserver and tools are present on the destination. If that is the case, uninstall it using the **state=absent** keyword of playbook.

Dependencies
------------

The PHP role depends on this Apache role to be installed first. We have mentioned the same information in the other role.

Example Playbook
----------------
In the directory **Apache/tasks/main.yml**, enter the following information:

```yml
---
# tasks file for apache
- name: Ensure that apache httpd is not installed in the framework
  yum: name=httpd state=absent
- name: Ensure httpd-tools service is not installed
  yum: name=httpd-tools state=absent

```

License
-------

BSD

Author Information
------------------

Gaurav Tripathi
