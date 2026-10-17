#   Context Parameter Map

An object that contains a key-value pair where the keys are the names of the context parameters and its values being the type of context parameter and its corresponding value provider.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`<name>` | [Entry](#entry) | | The context parameter to provide. The `<name>` can be arbitrary as long as it follows the rules of [identifiers]({{ mc.identifier }}).

[](){ #entry }

???+ info "Entry"

    An object that defines a context parameter.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `type` | Parameter Type | | The type of the context parameter.
    `value` | Value Provider | | The value provider to provide the value of the context parameter.


    ??? question "Parameter types and values"

        Defining a context parameter requires specifying its type. Refer to the table below for a collection of available context parameter types and its corresponding value provider:

        Parameter Type | Value Provider
        ---------------|---------------
        `neo-apoli:block` | [Block Provider][block_provider]
        `neo-apoli:boolean` | [Boolean Provider][boolean_provider]
        `neo-apoli:box` | [Box Provider][box_provider]
        `neo-apoli:command_source` | [Command Source Provider][command_source_provider]
        `neo-apoli:damage_source` | [Damage Source Provider][damage_source_provider]
        `neo-apoli:direction` | [Direction Provider][direction_provider]
        `neo-apoli:effect` | [Effect Provider][effect_provider]
        `neo-apoli:entity` | [Entity Provider][entity_provider]
        `neo-apoli:float` | [Float Provider][float_provider]
        `neo-apoli:int` | [Int Provider][int_provider]
        `neo-apoli:item` | [Item Provider][item_provider]
        `neo-apoli:nbt` | [NBT Provider][nbt_provider]
        `neo-apoli:slot` | [Slot Provider][slot_provider]
        `neo-apoli:string` | [String Provider][string_provider]
        `neo-apoli:vec3` | [Vec3 Provider][vec3_provider]


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
