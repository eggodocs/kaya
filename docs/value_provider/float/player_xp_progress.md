#   Player XP Progress

Provides the progress of a player for obtaining the next level.


Type ID: `kaya:player/xp/progress`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The player to get the progress from.


### Example

```json
{
    "type": "kaya:linear_interpolated",
    "delta": {
        "type": "kaya:player/xp/progress",
        "entity": "this"
    },
    "start": 1.0,
    "end": 0.0
}
```

This example provides the progress of the player provided by the `kaya:this_entity` context parameter, but in reverse *(from 1.0 to 0.0 instead of 0.0 to 1.0)*


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
