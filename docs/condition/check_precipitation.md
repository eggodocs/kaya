#   Check Precipitation

Checks the precipitation of a biome at the specified position.


Type ID: `neo-apoli:check_precipitation`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`precipitation` | [Precipitation][precipitation] | | The precipitation to match.
`position` | [Vec3 Provider][vec3_provider] | | The position of the biome to check the precipitation of.


### Example

```json
{
    "type": "neo-apoli:check_precipitation",
    "precipitation": "rain",
    "position": {
        "type": "neo-apoli:block/position",
        "block": "broken_block"
    }
}
```

This example will check if the precipitation of the biome at the position of the block provided by the `neo-apoli:broken_block` context parameter is rain.


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
