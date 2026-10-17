#   Context Parameter Map

An object that contains a key-value pair where the keys are the names of the context parameters and its values being the type of context parameter and its corresponding value provider.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`<name>` | [Entry](#entry) | | The context parameter to provide. The `<name>` will be the ID of the context parameter and it can be arbitrary as long as it follows the rules of [identifiers]({{ mc.identifier }}).


[](){ #entry }

???+ info "Entry"

    An object that defines a context parameter and its value.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `type` | [Context Parameter Type](../data/context_parameter.md#types) | | The ID of the desired parameter type.
    `value` | [Value Provider][value_provider] | | The value provider that'd provide the value for the parameter.


    ???+ tip

        Make sure to click on the hyperlink for context parameter types to see the corresponding value provider to use for your desired type.


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
