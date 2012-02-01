
Tabbed Interface
================

There are potentially two ways that we could achieve this:

#. Modify the admin templates - this will allow us to support URL parameters (e.g. /lesson/1/?active_tab=2)

#. Use javascript to show/ hide tabs.

In either case, we may want to add an alert if the user is about to leave the page without saving.


HTML Metadata
=============

seo_keywords should be generated from key_concepts


Inline Fields
=============

Django inline fields always appear at the bottom of a form. The only way to change this seems to be using javascript to move the inline fields higher on the form. One workaround might be to try to add links (e.g. back to top) above the inline fields, to allow admins to easier navigate the form.
