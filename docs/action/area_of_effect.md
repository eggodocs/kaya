#   Area of Effect

Executes an action on targets within the radius of an area.


Type ID: `neo-apoli:area_of_effect`


???+ info

    This type will provide the following context parameters to the `area_condition` and `area_action` fields when checking for targets and executing if fulfilled depending on the specified `area_target`:

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
`area_target` | [Area Target](#area_target) | | Determines what kind of target is affected by the area.
`area_action` | [Action][action] | | The action to execute on the targets.
`area_condition` | [Condition][condition] | *optional* | If specified, this condition is checked on each target before executing the `area_action`.
`position` | [Vec3 Provider][vec3_provider] | | The position of the area.
`shape` | [Shape][shape] | `"cube"` | The shape of the area.
`radius` | [Float Provider][float_provider] | | The radius of the area.


[](){ #area_target }

???+ info "Area target"

    A [string][string] that determines what kind of target is affected by an area.


    ### Values

    Value | Description
    ------|------------
    `entity` | The area will affect entities within it.
    `block` | The area will affect blocks within it.


### Example

```json
{
    "type": "neo-apoli:area_of_effect",
    "area_target": "entity",
    "area_action": {
        "type": "neo-apoli:set_entity_on_fire",
        "ticks": 200,
        "entity": "entity_in_area"
    },
    "area_condition": {
        "type": "neo-apoli:is_entity_of_type",
        "entity_type": "minecraft:creeper",
        "entity": "entity_in_area"
    },
    "position": {
        "type": "neo-apoli:entity/position",
        "entity": "this"
    },
    "radius": 16.0
}
```

This example will set entities within a 16.0 blocks cubical area on fire relative to the entity provided by the `neo-apoli:this_entity` context parameter.


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
