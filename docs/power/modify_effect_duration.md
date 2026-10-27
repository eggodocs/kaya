#   Modify Effect Duration

Modifies the duration of a status effect inflicted on the entity holding the power.


Type ID: `kaya:modify/effect/duration`


???+ info

    This type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `kaya:actor_entity` | The entity that inflicted the status effect.
    `kaya:target_entity` | The entity holding the power.
    `kaya:applied_effect` | The inflicted status effect.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`modifiers` | [Array][array] of [Modifiers][modifier] | | The modifiers to apply to the duration of an inflicted status effect.


### Example

```json
{
    "type": "kaya:modify/effect/duration",
    "modifiers": [
        {
            "type": "kaya:multiply_additive",
            "phase": "total",
            "amount": 1.0
        }
    ],
    "active_condition": {
        "type": "kaya:is_effect_of_type",
        "effect_type": "minecraft:poison",
        "effect": "applied_effect"
    }
}
```

This example doubles the duration of the Poison status effect.


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
