#   Entity Active Effects

Provides the count of active status effects of an entity.


Type ID: `neo-apoli:entity/active_effects`


???+ info

    This type provides the following context parameters to its `condition` when counting the status effects of an entity:

    Parameter | Description
    ----------|------------
    `neo-apoli:active_effect` | The active status effect instance of an entity.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | *optional* | If specified, this condition will be checked to each status effect when counting them.
`entity` | [Entity Provider][entity_provider] | | The entity to get the status effects from.


### Example

```json
{
    "type": "neo-apoli:entity/active_effects",
    "condition": {
        "type": "neo-apoli:is_effect_in_tag",
        "tag": "#example:is_harmful"/*(1)!*/,
        "effect": "active_effect"
    },
    "entity": "this"
}
```


1. The location of the file is `data/example/tags/mob_effect/is_harmful.json`


This example will provide the count of status effects that are included in the `#example:is_harmful` status effect tag from the entity provided by the `neo-apoli:this_entity` context parameter.


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
