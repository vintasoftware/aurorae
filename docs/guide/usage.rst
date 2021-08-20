======
Usage
======

This guide will teach you how to generate CNAB240 files for bulk payments and how to extend the library for different formats.


Before starting
---------------
Aurora uses Python type hinting for data validation and generation of fixed-width CNAB 240 files.
The library receives as inputs an spreadsheet that must be a match of the Pydantic model [Spreadsheet],
a general handler parses the initial data to an intermediary representation used by the CNAB240 module to generate files.
Different types of inputs are supported by library through the creation of new providers, check the [spreadsheet provider](providers/spreadsheet) for an example.


The library is organized to hide the complex logic of the file generation and expose a simple model for data handling. As consequence we have three areas:
* Spreadsheet models: each provider has his own class, which maps perfectly the source data
* Payroll models: represents the default format used to generate the CNAB files
* CNAB models: responsible for transforming the payroll into a CNAB file, contains all the complexity of the file.


Data format
-----------

The supported format is a spreadsheet with three sheets: Company, Employees, and Payments, each sheet has specific fields that match exactly the ones defined on [Spreadsheet].
The information of the spradsheet includes:

.. code-block::

    Company:
        - bank information
        - details of the company
        - address information

    Employee
        - bank information
        - address information
        - personal information

    Payment:
        - employee
        - details of the payment


A sample file can [be found here].

Generating the file
-------------------

After installing aurorae with pip, the commands ``generate_cnab`` and ``generate_cnab_sample`` are available. To check CLI options, run:

.. code-block:: bash

    $ generate_cnab --help

The mandatory parameter is the input file, you can also pass an output file name through ``--output_filename``.


Validating the file
-------------------
A debug file is also generated when using the command line. The file consists on a html file with the fields highlighted and the details specified:

.. image:: https://user-images.githubusercontent.com/397989/113344903-166a0380-9308-11eb-987a-a73f7d472f02.png
  :width: 800
  :alt: Debug file sample

An sample debug file can be found on [File].

Adding new data formats
-----------------------

This library was designed to support multiple data formats (for details `check our ADR <https://github.com/vintasoftware/aurorae/blob/ab0851bc5dd9d960d1464cee7b836857e90a72b6/docs/adr/0002_cnab_architecture_pydantic.md>`_).
If you are trying to support new formats you need to:

1. Create a new `provider`
2. Replicate your new format as pydantic models (like the ones on [Spreadsheet])
3. Create the `_mapping` on your pydantic models to our common `Payroll` model (like the ones on [Spreadsheet])
4. Replicate the handler behavior using your newly created claass

Feel free to open a Pull Request with this new format.


Example
-------

The library comes with a built-in configuration to generate a sample cnab:


.. code-block:: bash

    $ generate_cnab_sample


