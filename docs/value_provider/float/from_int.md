#   From Int

Provides an integer converted as a float.


Type ID: `kaya:from_int`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Int Provider][int_provider] | | The integer value to convert as a float.


### Example

```json
{
    "type": "kaya:from_int",
    "value": {
        "type": "kaya:item/count",
        "item": "used_item"
    }
}
```

This example will get the count of the item provided by the `kaya:used_item` context parameter and converts it as a float.


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
