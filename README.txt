Admin documentation for lettuce-generated integration tests.
-------------------------------------

This module integrates lettuce (http://www.lettuce.it) support for Django by
printing out the content of the features and scenarios to the Django admin
interface.

The goal is to make the final user aware of the specifications and requirements
of the application without having to browse the source code.

To install this module in a Django application with lettuce features:
* install the module (for instance, using pip)
* add 'adminlettuce' to the INSTALLED_APPS in settings.py
* add a route to 'adminlettuce' in urls.py, for instance:
  (r'^admin/features/',     include('adminlettuce.urls')),
