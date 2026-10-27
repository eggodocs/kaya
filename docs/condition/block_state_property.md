#   Block State Property

Checks if a state property of a block matches a specified value.


Type ID: `kaya:block_state_property`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`property` | [String Provider][string_provider] | | The state property to check the value of.
`block` | [Block Provider][block_provider] | | The block to get the state property from.
`value` | [String Provider][string_provider] | | The value to compare to.


### Example

```json
{
    "type": "kaya:block_state_property",
    "property": "axis",
    "block": "broken_block",
    "value": "y"
}
```

This example will check if the `axis` state property of the block provided by the `kaya:broken_block` context parameter is equal to `"y"`.


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
