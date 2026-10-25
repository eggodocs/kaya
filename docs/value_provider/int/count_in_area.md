#   Count in Area

Counts how many entities/blocks are within the specified area.


Type ID: `neo-apoli:count_in_area`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`area` | [Area][area] | | The area to get the entities/blocks from.
`condition` | [Condition][condition] | *optional* | If specified, only count the entities/blocks that fulfill this condition.
`limit` | [Int Provider][int_provider] | *optional* | If specified, the counting will be ended early if the count reaches this value, unless it's 0 or a negative value.


### Example

```json
{
    "type": "neo-apoli:count_in_area",
    "area": {
        "type": "neo-apoli:box",
        "target": "entity",
        "shape": "star",
        "box": {
            "type": "neo-apoli:inflate",
            "box": {
                "type": "neo-apoli:entity/bounds",
                "entity": "this"
            },
            "vector": [
                2.0,
                0.0,
                2.0
            ]
        }
    },
    "condition": {
        "type": "neo-apoli:check_entity_type",
        "key": "minecraft:creeper",
        "entity": "this"
    }
}
```

This example will count how many creepers are within the bounding box of the entity provided by the `neo-apoli:this_entity` context parameter, inflated by 2 blocks in the horizontal directions.


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
