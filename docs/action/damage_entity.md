#   Damage Entity

Deals damage to an entity.


Type ID: `neo-apoli:damage_entity`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`damage_type` | [Identifier]({{ mc.damage_type_identifier }}) | | The ID of the damage type to use.
`amount` | [Float Provider][float_provider] | | The amount of damage to deal.
`victim` | [Entity Provider][entity_provider] | | The entity that will be damaged.
`attacker` | [Entity Provider][entity_provider] | *optional* | If specified, this entity will be considered as the source of the damage.


### Example

```json
{
    "type": "neo-apoli:damage_entity",
    "damage_type": "minecraft:magic",
    "amount": {
        "type": "neo-apoli:random/uniform",
        "min": 1.0,
        "max": 8.0
    },
    "victim": "target",
    "attacker": "actor"
}
```

This example will deal a random amount (ranging from $1.0$ to $8.0$) of damage to the entity provided by the `neo-apoli:target_entity` context parameter, making the entity provided by the `neo-apoli:actor_entity` context parameter as the source of the damage.


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
