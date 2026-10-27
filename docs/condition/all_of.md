#   All Of

Checks if all of the conditions are fulfilled.


Type ID: `kaya:all_of`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`conditions` | [Array][array] of [Conditions][condition] | | The conditions to check.


### Example

```json
{
    "type": "kaya:all_of",
    "conditions": [
        {
            "type": "kaya:is_entity_sneaking",
            "entity": "this"
        },
        {
            "type": "kaya:check_block_type",
            "key": "minecraft:oak_log",
            "block": "broken_block"
        }
    ]
}
```

This example will check if the entity provided by the `kaya:this_entity` context parameter is sneaking **and** if the block provided by the `kaya:broken_block` context parameter is an Oak log.


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
