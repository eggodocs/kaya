#   Check Block Type

Check if a block is of a type or if it's included in a block tag.


Type ID: `kaya:check_block_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`key` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, checks if the block is of this specific type.
`tag` | [Block Tag]({{ mc.block_tag }}) | *optional* | If specified, checks if the block is included in this block tag.
`block` | [Block Provider][block_provider] | | The block to check.


???+ warning

    Both `key` and `tag` fields should **not** be present or absent at the same time! Otherwise an error will be thrown.


### Example

```json
{
    "type": "kaya:check_block_type",
    "tag": "#minecraft:planks",
    "block": "broken_block"
}
```

This example will check if the block provided by the `kaya:broken_block` context parameter is included in the `#minecraft:planks` block tag.


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
