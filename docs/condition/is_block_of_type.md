#   Is Block of Type

Check if a block is of a specific block type.


Type ID: `neo-apoli:is_block_of_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`block_type` | [Identifier]({{ mc.identifier }}) | | The ID of the block type.
`block` | [Block Provider][block_provider] | | The block to check.


### Example

```json
{
    "type": "neo-apoli:is_block_of_type",
    "block_type": "minecraft:dirt",
    "block": {
        "type": "neo-apoli:world",
        "position": [
            0.0,
            63.0,
            0.0
        ]
    }
}
```

This example will check if the block at 0, 63, 0 is a dirt block.


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
