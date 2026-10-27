#   Modify Invisibility

Modifies whether the entity holding the power should be invisible and whether they should be invisible to a specific entity.


Type ID: `kaya:modify/invisibility`


???+ info

    This type provides the following context parameters:

    Parameter | Description
    ----------|------------
    `kaya:actor_entity` | The entity seeing the entity holding the power.
    `kaya:target_entity` | The entity holding the power.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`invisible_to_condition` | [Condition][condition] | *optional* | If specified, the entity holding the power will only be invisible to an entity if this evaluates to true. Otherwise, the entity will appear translucent.
`render_armor` | [Boolean Provider][boolean_provider] | `true` | Determines whether the armor layer should render when the entity is invisible.
`render_outline` | [Boolean Provider][boolean_provider] | `true` | Determines whether the glowing outline should render when the entity is invisible.


### Example

```json
{
    "type": "kaya:modify/invisibility",
    "invisible_to_condition": {
        "type": "kaya:inverted",
        "condition": {
            "type": "kaya:entity_has_power",
            "power": "*:*",
            "entity": "target"
        }
    },
    "render_armor": {
        "type": "kaya:condition_result",
        "condition": {
            "type": "kaya:inverted",
            "condition": {
                "type": "kaya:is_entity_sneaking",
                "entity": "this"
            }
        }
    }
}
```

This example will make the entity invisible to other entities except those that has the same power (in which, the entity will appear translucent.) The armor layer will also be hidden if the entity is sneaking.


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
