#   Block

Provides a command source based from a block, where the position and name of the command source is the position and name of the block.


Type ID: `kaya:block`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`block` | [Block Provider][block_provider] | | The block to create the command source from.


### Example

```json
{
    "type": "kaya:block",
    "block": "mined_block"
}
```

This example provides a command source where its position and name used in the command source is the position and name of the block provided by the `kaya:mined_block` context parameter.


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
