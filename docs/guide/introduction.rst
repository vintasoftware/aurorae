===============
Introduction
===============


What is a CNAB240
-----------------

CNAB240 is a standard defined by FEBRABAN and implemented by Brazilian
banks for the exchange of information between companies and banks. Based
on the information necessary for the implementation of each type of
service, the standard defines a set of records/fields that must compose
the exchange file.

The standard covers the following types of services:

* **Payment via account credit (Pagamento através de crédito em conta, cheque, OP, DOC ou pagamento com autenticação)**
* Payment of bills of exchange (Pagamento de títulos de Cobrança)
* Tax payments (Pagamento de Tributos)
* Billing Securities (Títulos em Cobrança)
* Electronic Payment Slip (Boleto de Pagamento Eletrônico)
* Payer's Claim (Alegação do Pagador)
* Checking Account Statement for Bank Reconciliation (Extrato de Conta Corrente para Conciliação Bancária)
* Direct debit (Débito em Conta Corrente)
* Vendor (Vendor)
* Custody of Checks (Custódia de Cheques)
* Statement for Cash Management (Extrato para Gestão de Caixa)
* Loan with Payroll Consignment (Empréstimo com Consignação em Folha de Pagamento)
* Buy (Compror)

Aurorae only supports Payment via account credit.

CNAB versions
-------------

The versions of the file are identified through a code with the
following composition: VV.R

* VV: Version number
* R: Release number

Aurorae only supports the version 10.7 of CNAB240.

File Structure
--------------

The exchange file is composed of a file header record, one or more
service/product batches and a file trailer record.

::

        File Header
            Batch
                Batch Header
                Initial Batch Records
                Segment Detail Records
                Final Batch Records
                Batch Trailer
        Filte Trailer

A single file can contain multiple batches of different Services. Each
of the items described above represent one line of the file with the
size of 240 bytes. Individuals fields for each line are aligned
according to the type of the field:

* Numeric Fields (Num) = Always on the right and padded with zeros on the left.
* Alphanumeric Fields (Alpha) = Always on the left and filled with blanks on the right.

Payment via account credit
~~~~~~~~~~~~~~~~~~~~~~~~~~

This service batch is composed of a batch header record, one or more
detail records, and a batch trailer record, besides, the same batch can
be used to send information or to receive information. The types of
detail segments for this batch are:

::

        Shipping
            A (mandatory)
            B (mandatory)
            C (optional)

        Return
            A (mandatory)
            B (optional)
            C (optional)

Aurorae doesn't support sending the detail segment C yet.

Summary
-------

-  Aurorae only supports Payment via account credit
-  Aurorae only supports the version 10.7 of CNAB240
-  Aurorae doesn't support sending the detail segment C
