#   Context Parameter Map

An object that contains a key-value pair where the keys are the names of the context parameters and its values being the type of context parameter and its corresponding value provider.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`<name>` | [Context Parameter][context_parameter] | | The context parameter to provide. The `<name>` will be the ID of the context parameter and it can be arbitrary as long as it follows the rules of [identifiers]({{ mc.identifier }}).


### Example

```json
{
    "example:random_int": {
        "type": "neo-apoli:int",
        "value": {
            "type": "neo-apoli:random/uniform",
            "min": 1,
            "max": 64
        }
    },
    "example:held_entity": {
        "type": "neo-apoli:entity",
        "value": "this"
    }
}
```

This example provides a context parameter map that has two context parameters: `example:random_int` which refers to a random integer from 1 to 64, and `example:held_entity` which refers to the entity from the `neo-apoli:this_entity` context parameter.
