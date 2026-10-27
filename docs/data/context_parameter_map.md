#   Context Parameter Map

An object that contains a key-value pair where the keys are the names of the context parameters and its values being the type of context parameter and its corresponding value provider.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`<name>` | [Value Provider][value_provider] | | The context parameter and its value provider. The `<name>` will be the ID of the context parameter and it can be arbitrary as long as it follows the rules of [identifiers]({{ mc.identifier }}).


### Example

```json
{
    "example:random_int": {
        "type": "kaya:int",
        "value": {
            "type": "kaya:random/uniform",
            "min": 1,
            "max": 64
        }
    },
    "example:held_entity": {
        "type": "kaya:entity",
        "value": "this"
    }
}
```

This example provides a context parameter map that has two context parameters with certain value providers:

- `example:random_int`, which has an [int provider][int_provider] that refers to a random integer with the range of 1 to 64.
- `example:held_entity`, which has an [entity provider][entity_provider] that refers to the entity provided by the `kaya:this_entity` context parameter.
