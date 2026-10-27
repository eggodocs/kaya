#   Block Bounds

Provides the shape of a block as a box.


Type ID: `kaya:block/bounds`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`shape_type` | [Shape Type][shape_type] | | Determines which type of shape of the block should be queried.
`block` | [Block Provider][block_provider] | | The block to get its shape transformed into a block from.


### Example

```json
{
    "type": "kaya:block/bounds",
    "shape_type": "outline",
    "block": "used_block"
}
```

This example provides the shape transformed into a box of the block provided by the `kaya:used_block` context parameter.


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
