#   Int { #int_comparison }

Compares the first and second integers.


Type ID: `neo-apoli:int`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`comparator` | [Comparator][comparator] | | Determines how the integers are compared.
`first` | [Int Provider][int_provider] | | The first integer to compare to.
`second` | [Int Provider][int_provider] | | The second integer to be compared.


### Example

```json
{
    "type": "neo-apoli:int",
    "comparator": ">=",
    "first": {
        "type": "neo-apoli:count_in_area",
        "area": {
            "type": "neo-apoli:radius",
            "target": "entity",
            "shape": "cube",
            "position": {
                "type": "neo-apoli:entity/position",
                "entity": "this"
            },
            "radius": 16.0
        },
        "condition": {
            "type": "neo-apoli:check_entity_type",
            "key": "minecraft:creeper",
            "entity": "entity_in_area"
        }
    },
    "second": 8
}
```

This example checks if the count of Creepers within a 16 block cubical radius relative to the entity provided by the `neo-apoli:this_entity` context parameter is greater or equal to 8.


### History

<table>
    <tr>
        <td style="text-align: center; vertical-align: middle"><b>Minecraft</b></td>
        <td style="text-align: center; vertical-align: middle"><b>Mod</b></td>
        <td style="vertical-align: middle"><b>Changelog</b></td>
    </tr>
    <tr style="text-align: center; vertical-align: middle">
        <td style="text-align: center; vertical-align: middle">1.21.5</td>
        <td style="text-align: center; vertical-align: middle">0.1.0</td>
        <td style="vertical-align: middle">Added the type.</td>
    </tr>
</table>
