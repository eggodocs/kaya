#   Modify Falling

Modifies the falling velocity of the entity holding the power and optionally whether it should take fall damage or not.


Type ID: `kaya:modify/falling`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`modifiers` | [Array][array] of [Modifiers][modifier] | | The modifiers to apply to the falling velocity of the entity.
`take_fall_damage` | [Boolean Provider][boolean_provider] | `true` | Determines whether the entity should take fall damage.


### Example

```json
{
    "type": "kaya:modify/falling",
    "modifiers": [
        {
            "type": "kaya:set",
            "phase": "base",
            "amount": 0.01
        }
    ],
    "take_fall_damage": false,
    "active_condition": {
        "type": "kaya:inverted",
        "condition": {
            "type": "kaya:is_entity_sneaking",
            "entity": "this"
        }
    }
}
```

This example makes the entity fall very slowly (akin to the Slow Falling status effect) if they're not sneaking.


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
