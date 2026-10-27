#   Rain Level

Provides the rain level of the current dimension.


Type ID: `kaya:rain_level`


???+ note  
    
    This type will provide nothing if the dimension doesn't have sky light or if it has a ceiling.


???+ tip
    
    If rain level is greater than 0.2, it's considered raining in the dimension.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`delta` | [Float Provider][float_provider] | `1.0` | The percentage used for the interpolation between the old and current rain level value of the dimension. The value is clamped within the range of 0.0 to 1.0.


### Example

```json
{
    "type": "kaya:rain_level"
}
```

This example provides the current rain level of the dimension.


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
