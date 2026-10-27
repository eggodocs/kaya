#   Player Saturation

Provides the saturation value of a player.


Type ID: `kaya:player/saturation`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The player to get the saturation of.


### Example

```json
{
    "type": "kaya:player/saturation",
    "entity": "damaging_entity"
}
```

This example will provide the saturation level of a player *(provided by the `kaya:damaging_entity` context parameter.)*


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
