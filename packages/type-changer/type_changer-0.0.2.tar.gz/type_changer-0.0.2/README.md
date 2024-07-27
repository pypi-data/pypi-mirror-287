# Data-Type Caster

This project aim is to convert the given json or dictionary format structure to same structure with values of desired data-type, Which is achived using Pydantic Basemodel.

## Installation
### PIP
```
pip install type-changer
```

## Usage
```
from pydantic import BaseModel
from type_changer import Caster

class model(BaseModel):
    a:str
    b:int
    c:list[str]

input = {"a":"hello", "b":"45327", "c":[34,45,56]}

ct = Caster(model, input)
out = ct.cast()
print(out)
```

### Note:
 - This project consider your input is a valid json or dictionary.
 - Create a Basemodel class for every dict in the json or dictionary.
 - This project supports only the following data-types which are 'str', 'int', 'float', 'list', 'tuple' and 'bool'.

## License
This project is licensed under AGPL-3 license and 'All rights Reserved'. For more details see the LICENSE file.
