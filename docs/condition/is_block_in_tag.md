#   Is Block In Tag

Checks if a block is in a specified block tag.


Type ID: `neo-apoli:is_block_in_tag`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`tag` | [Block Tag]({{ mc.block_tag }}) | | The block tag to match.
`block` | [Block Provider][block_provider] | | The block to check.


### Example

```json
{
    "type": "neo-apoli:is_block_in_tag",
    "tag": "#minecraft:convertable_to_mud",
    "block": "broken_block"
}
```

This example will check if the block provided by the `neo-apoli:broken_block` context parameter is included in the `#minecraft:convertable_to_mud` block tag.


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
