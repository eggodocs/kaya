#   Gain Air

Increases/decreases the entity's air supply.


Type ID: `neo-apoli:gain_air`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Int Provider][int_provider] | | The amount to increase/decrease to/from the entity's air supply.
`entity` | [Entity Provider][entity_provider] | | The entity to increase/decrease the air supply of.


### Example

```json
{
    "type": "neo-apoli:gain_air",
    "value": 5,
    "entity": "this"
}
```

This example increases the air supply of the entity provided by the `neo-apoli:this_entity` context parameter by $5$.


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
