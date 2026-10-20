#   Effect Amplifier

Provides the amplifier of a [status effect instance][status_effect_instance] from an entity.


Type ID: `neo-apoli:effect/amplifier`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`effect` | [Identifier]({{ mc.effect_identifier }}) | | The ID of the status effect.
`entity` | [Entity Provider][entity_provider] | | The entity to get the status effect from.


### Example

```json
{
    "type": "neo-apoli:effect/amplifier",
    "effect": "minecraft:poison",
    "entity": "this"
}
```

This example provides the amplifier of the Poison status effect from an entity *(provided by the `neo-apoli:this_entity` context parameter.)*


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
