#   Is Sky Visible

Checks if the sky is visible at the specified position.


Type ID: `neo-apoli:is_sky_visible`


???+ note

    Not to be confused with [Is Exposed to Sky](is_exposed_to_sky.md), which also checks if there are no blocks between the sky and the specified position.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to check.


### Example

```json
{
    "type": "neo-apoli:is_sky_visible",
    "position": {
        "type": "neo-apoli:entity/position",
        "entity": "this"
    }
}
```

This example checks if the position of the entity provided by the `neo-apoli:this_entity` context parameter is exposed to the sky.


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
