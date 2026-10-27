#   World

Provides the block at the specified position.


Type ID: `kaya:world`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to get the block from.


### Example

```json
{
    "type": "kaya:world",
    "position": {
        "type": "kaya:block/position",
        "block": "mined_block"
    }
}
```

This example provides the block provided by the `kaya:mined_block` context parameter.


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
