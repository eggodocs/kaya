#   Block Position

Provides the position of a block.


Type ID: `kaya:block/position`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`block` | [Block Provider][block_provider] | | The block to get the position from.


### Example

```json
{
    "type": "kaya:block/position",
    "block": "used_block"
}
```

This example provides the position of the block provided by the `kaya:used_block` context parameter.


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
