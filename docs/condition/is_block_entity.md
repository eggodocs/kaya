#   Is Block Entity

Checks if a block is a block entity.


Type ID: `kaya:is_block_entity`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`block` | [Block Provider][block_provider] | | The block to check.


### Example

```json
{
    "type": "kaya:is_block_entity",
    "block": "used_block"
}
```

This example will check if the block provided by the `kaya:used_block` context parameter is a block entity.


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
