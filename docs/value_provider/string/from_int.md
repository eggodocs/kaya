#   From Int

Stringifies an integer and uses it as the provided value.


Type ID: `kaya:from_int`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Int Provider][int_provider] | | The integer to stringify.


### Example

```json
{
    "type": "kaya:from_int",
    "value": {
        "type": "kaya:item/fuel",
        "item": "used_item"
    }
}
```

This example stringifies the fuel value of the item provided by the `kaya:used_item` context parameter.


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
