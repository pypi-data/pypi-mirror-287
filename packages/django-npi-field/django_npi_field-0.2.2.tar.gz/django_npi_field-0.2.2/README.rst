################
django-npi-field
################

Description
===========
**Django-npi-field** is a Django library which validates and stores 10-digit U.S. `National Provider Identifier (NPI)`_
numbers using a custom Luhn algorithm. [1]_

.. _`National Provider Identifier (NPI)`: \
   https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand

Installation
============
From PyPI
---------
Using pip:

.. code-block:: zsh

   pip install django-npi-field

Using poetry:

.. code-block:: zsh

   poetry add django-npi-field

From GitHub
-----------
Using poetry:

.. code-block:: zsh

   poetry add git+https://github.com/PhoenixStorm1015/django-npi-field.git

Usage
=====
Setup
-----
Add the app to ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code-block:: python

   INSTALLED_APPS = [
       # Other apps...
       "npi_field",
   ]

Adding the model field
----------------------
Add the field to your ``models.py``.

.. code-block:: python

   from django.db import models
   from npi_field.modelfields import NPIField

   class HealthcareProvider(models.Model):
       npi = NPIField()

Using the form field
--------------------
In a default ``ModelForm``, the package's custom form field with its length restrictions is automatically used. You can
add it to a normal form as follows:

.. code-block:: python

   from django import forms
   from npi_field.formfields import NPIField

   class NPIForm(forms.Form):
       npi = NPIField()

Calling the validator directly
------------------------------
If you prefer, you can also call the validator directly. If you want the length restriction in the model field, make
sure to also set the ``max_length`` argument. This won't affect the validator, as it checks that the value is 10
characters long before running the algorithm.

.. code-block:: python

   from django.db import models
   from npi_field.validators import npi_validator

   class HealthcareProvider(models.Model):
       npi = models.CharField(max_length=10, validators = [npi_validator])

.. [1] **NOTE:** This is a Luhn algorithm specially implemented for NPI numbers due to it's shorter length. This \
   library **WON'T WORK** for other numbers validated by a Luhn algorithm, such as credit/debit card \
   numbers, ISBN numbers, or IMEI numbers.