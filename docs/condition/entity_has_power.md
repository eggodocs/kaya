#   Entity Has Power

Checks if an entity has a specified power, and optionally, if it's from a specific source.


Type ID: `neo-apoli:entity_has_power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The ID of the power to check for.
`source` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, checks if the power was granted with this ID as its source.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "neo-apoli:entity_has_power",
    "power": "thing:really_cool",
    "entity": "this"
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter has the `thing:really_cool` power.


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
