#   Apply Effects

Apply status effects to an entity.


Type ID: `neo-apoli:apply_effects`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`effects` | [Array][array] of [Effect Providers][effect_provider] | | The status effects to apply to the entity.
`entity` | [Entity Provider][entity_provider] | | The entity to apply the status effects to.


### Example

```json
{
    "type": "neo-apoli:apply_effects",
    "effects": [
        {
            "id": "minecraft:regeneration",
            "amplifier": 1,
            "duration": 100
        }
    ],
    "entity": "this"
}
```

This example will apply the Regeneration II (00:05) status effect to the entity from the `neo-apoli:this_entity` context parameter.


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
