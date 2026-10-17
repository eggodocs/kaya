#   Power

Encodes the data of the referenced power as NBT and uses it as the provided value.


Type ID: `neo-apoli:power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The ID of the power to encode as NBT.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "neo-apoli:power",
    "power": "example:power",
    "entity": "this"
}
```

This example encodes the data of the `example:power` power from the entity provided by the `neo-apoli:this_entity` context parameter.


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
