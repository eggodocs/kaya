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
        "type": "neo-apoli:entities_in_radius",
        "condition": {
            "type": "neo-apoli:is_entity_of_type",
            "entity_type": "minecraft:creeper",
            "entity": "target"
        },
        "position": {
            "type": "neo-apoli:entity/position",
            "entity": "this"
        },
        "shape": "cube",
        "radius": 16.0
    },
    "second": 8
}
```

This example checks if the count of Creepers within a 16 block cubical radius is greater or equal to 8.


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
