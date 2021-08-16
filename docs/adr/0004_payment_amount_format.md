# Payment Amount Format
Date: 16-08-2021


## Status
- Accepted


## Context
Currency formats differ from country to country. An example is in the United States (U.S.), the currency is formatted with a decimal point **(.)** as a separator between the dollars and cents. Some countries use a comma **(,)** instead of decimal to indicate that separation. The payment amount is a critical value for the functionality of this library and accepts two decimal places. To avoid format errors, standardization is required.


## Decision
We decided to define a single format for monetary fields with decimal places. The format is:
- We only receive monetary values as integers.
- Decimal places should be added as zeros or the respective values

eg:

- R$ 100,00    -> 10000
- R$ 100.00    -> 10000
- R$ 1.000,00  -> 100000


The type to represent this field is mapped on `types.PaymentAmount`, this is type inherits from a general format used by other fields. Any other format will raise an error.

We based this decision on a public API of a brazilian bank called Nubank. Attributes used to display information to the users are formatted with the correct currency format, but other payment/credit/debit amounts are saved as integers.

## Consequences
- We have a unified way of receiving monetary values
- We need to make this clear to the user
