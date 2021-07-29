# Ubiquitous Language of CNAB Fields
Date: 22-07-2021


## Status
- Accepted


## Context
The CNAB models currently don't detail the fields. Therefore it's hard to know which fields we are mentioning. Moreover, when using pydantic `Model.schema()`, the final JSON schema still requires you to check the final CNAB for a better understanding.


## Decision
Use pydantic [Field](https://pydantic-docs.helpmanual.io/usage/schema/) to improve the schema specification.

```python
from pydantic import Field as FieldSchema


class HeaderCNAB(BaseModel):
    field_01_0: CodigoBanco = FieldSchema(
        description="Código do Banco na Compensação", code="01.0"
    )
```

## Consequences
- Improved and understandable JSON Schemas
