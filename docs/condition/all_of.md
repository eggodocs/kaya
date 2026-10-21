#   All Of

Checks if all of the conditions are fulfilled.


Type ID: `neo-apoli:all_of`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`conditions` | [Array][array] of [Conditions][condition] | | The conditions to check.


### Example

```json
{
    "type": "neo-apoli:all_of",
    "conditions": [
        {
            "type": "neo-apoli:is_entity_sneaking",
            "entity": "this"
        },
        {
            "type": "neo-apoli:is_block_of_type",
            "block_type": "minecraft:oak_log",
            "block": "broken_block"
        }
    ]
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter is sneaking **and** if the block provided by the `neo-apoli:broken_block` context parameter is an Oak log.


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
