#   Is Entity Stepping on Block

Checks if an entity is stepping on a block.


Type ID: `neo-apoli:is_entity_stepping_on_block`


???+ info

    This type provides the following context parameters to its `stepped_on_condition` field when checking for the block being stepped on by an entity:

    Parameter | Description
    ----------|------------
    `neo-apoli:stepped_on_block` | The block being stepped on by an entity.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`stepped_on_condition` | [Condition][condition] | *optional* | If specified, this condition is checked on the block being stepped on by the entity.
`entity` | [Entity Provider][entity_provider] | | The entity to get the stepped block from.


### Example

```json
{
    "type": "neo-apoli:is_entity_stepped_on_block",
    "stepped_on_condition": {
        "type": "neo-apoli:check_block_type",
        "tag": "#minecraft:carpets",
        "block": "stepped_on_block"
    },
    "entity": "this"
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter is stepping on a block included in the `#minecraft:carpets` block tag.


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
