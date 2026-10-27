#   Direction { #direction_direction_provider_type}

Provides the unit vec3 of a direction.


Type ID: `kaya:direction`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`direction` | [Direction Provider][direction_provider] | | The direction to get the unit vec3 from.


### Example

```json
{
    "type": "kaya:direction",
    "direction": "up"
}
```

This example provides the unit vec3 of the up direction, which will be a vec3 with X, Y, and Z coordinates of 0, 1, and 0 respectively.


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
