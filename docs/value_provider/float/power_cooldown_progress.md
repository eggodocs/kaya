#   Power Cooldown Progress

Provides the progress of the cooldown of a power from an entity.


Type ID: `kaya:power/cooldown/progress`


???+ tip

    A value of $1.0$ means that the power has cooled down.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The ID of the power to get the cooldown of.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.


### Example

```json
{
    "type": "kaya:power/cooldown/progress",
    "power": "example:fire_ball@cooldown",//(1)!
    "entity": "this"
}
```


1. This is referring to the sub-power, `cooldown`, defined in a super-power with the ID `example:fire_ball` and a location of `data/example/kaya/powers/fire_ball.json`


This example will provide the cooldown progress of the `example:fire_ball@cooldown` sub-power from an entity *(provided by the `kaya:this_entity` context parameter.)*


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
