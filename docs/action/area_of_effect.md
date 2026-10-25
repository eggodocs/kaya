#   Area of Effect

Executes an action on targets within the radius of an area.


Type ID: `neo-apoli:area_of_effect`


???+ info

    This type will provide the following context parameters to the `action` and `condition` fields when checking for targets and executing if fulfilled depending on the area's specified target:

    === "`entity`"

        Parameter | Description
        ----------|------------
        `neo-apoli:entity_in_area` | The affected entity in the specified area.

    
    === "`block`"

        Parameter | Description
        ----------|------------
        `neo-apoli:block_in_area` | The affected block in the specified area.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`area` | [Area][area] | | The area to get the targets from.
`action` | [Action][action] | | The action to execute to the targets.
`condition` | [Condition][condition] | *optional* | If specified, only targets that fulfill this condition will have the action executed on them.
`limit` | [Int Provider][int_provider] | *optional* | If specified, the iteration will be ended early if this amount of targets have been processed, unless it's 0 or a negative value.


### Example

```json
{
    "type": "neo-apoli:area_of_effect",
    "area": {
        "type": "neo-apoli:radius",
        "target": "entity",
        "shape": "cube",
        "position": {
            "type": "neo-apoli:entity/position",
            "entity": "this"
        },
        "radius": 16.0
    },
    "action": {
        "type": "neo-apoli:set_entity_on_fire",
        "ticks": 200,
        "entity": "entity_in_area"
    },
    "condition": {
        "type": "neo-apoli:check_entity_type",
        "key": "minecraft:creeper",
        "entity": "entity_in_area"
    }
}
```

This example will set creeprs on fire within a 16.0 blocks cubical area relative to the position of the entity provided by the `neo-apoli:this_entity` context parameter.


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
