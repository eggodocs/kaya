#   Entity

Provides the slot from an entity.


Type ID: `neo-apoli:entity`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to get the slot from.
`slot` | [Int Provider][int_provider] | | The numerical ID of the slot to get from the entity.


### Example

```json
{
    "type": "neo-apoli:entity",
    "block": "this",
    "slot": {
        "type": "neo-apoli:slot_id",
        "slot": "hotbar.9"
    }
}
```

This example provides the 9th hotbar slot of the entity provided by the `neo-apoli:this_entity` context parameter.


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
