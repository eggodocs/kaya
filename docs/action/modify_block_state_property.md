#   Modify Block State Property

Modifies the state property of a block.


Type ID: `kaya:modify_block_state_property`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`property` | [String Provider][string_provider] | | The state property of the block to modify.
`block` | [Block Provider][block_provider] | | The block to modify its state property of.
`value` | [String Provider][string_provider] | *optional* | If specified, the value of the state property will be set to this value. 
`cycle` | [Boolean Provider][boolean_provider] | *optional* | If specified, the value of the state property will be cycled.


???+ warning

    Only one of `value` or `cycle` fields must be present! If both or none are present, an error will be thrown.


### Example

```json
{
    "type": "kaya:modify_block_state_property",
    "property": "axis",
    "block": "used_block",
    "cycle": true
}
```

This example will cycle the `axis` state property of the block provided by the `kaya:used_block` context parameter, essentially rotating the block.


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
