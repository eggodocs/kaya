#   Modify Climbing

Modifies whether an entity is considered climbing.


Type ID: `kaya:modify/climbing`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`holding_condition` | [Condition][condition] | `{"type": "kaya:is_entity_sneaking", "entity": "this"}` | Determines when an entity is considered holding onto a block.
`allow_holding` | [Boolean Provider][boolean_provider] | `true` | Determines whether "holding" onto a block is allowed.


### Example

```json
{
    "type": "kaya:modify/climbing",
    "active_condition": {
        "type": "kaya:compare",
        "comparison": {
            "type": "kaya:int",
            "comparator": ">=",
            "first": {
                "type": "kaya:blocks_intersecting_box",
                "condition": {
                    "type": "kaya:check_block_type",
                    "key": "minecraft:sugar_cane",
                    "block": "block_intersecting_box"
                },
                "box": {
                    "type": "kaya:entity/bounds",
                    "entity": "this"
                }
            },
            "second": 1
        }
    }
}
```

This example allows entities to climb in sugar canes.


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
