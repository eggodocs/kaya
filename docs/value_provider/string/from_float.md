#   From Float

Stringifies a float and uses it as the provided value.


Type ID: `kaya:from_float`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Float Provider][float_provider] | | The float to stringify.


### Example

```json
{
    "type": "kaya:from_float",
    "value": {
        "type": "kaya:player/saturation",
        "entity": "this"
    }
}
```

This example stringifies the food saturation value of the player provided by the `kaya:this_entity` context parameter.


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
