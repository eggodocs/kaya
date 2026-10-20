#   Blocks Colliding Box

Provides the count of blocks which fulfills a condition colliding with a box.


Type ID: `neo-apoli:blocks_colliding_box`


???+ info

    This type provides the following context parameters when checking the blocks colliding with the box:

    Parameter | Description
    ----------|------------
    `neo-apoli:block_colliding_box` | The block colliding to the box.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check on the blocks colliding with the box.
`box` | [Box Provider][box_provider] | | The box to use to check for blocks.


### Example

```json
{
    "type": "neo-apoli:blocks_colliding_box",
    "condition": true,
    "box": {
        "type": "neo-apoli:inflate",
        "box": {
            "type": "neo-apoli:entity/bounds",
            "entity": "this"
        },
        "vector": [
            1.0,
            1.0,
            1.0
        ]
    }
}
```

This example provides the count of blocks colliding with the bounding box *(inflated by 1 block)* of an entity *(provided by the `neo-apoli:this_entity` context parameter.)*


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
