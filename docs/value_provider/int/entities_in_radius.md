#   Entities in Radius

Provides the count of entities which fulfills a condition within an area with a shape and radius.


Type ID: `neo-apoli:entities_in_radius`


???+ info

    This type provides the following context parameters when checking the blocks within the radius of the area:

    Parameter | Description
    ----------|------------
    `neo-apoli:entity_in_radius` | The entity within the radius of the area.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to check on the block within the area.
`position` | [Vec3 Provider][vec3_provider] | | The position of the area.
`shape` | [Shape][shape] | | The shape of the area.
`radius` | [Float Provider][float_provider] | | The radius of the area.


### Example

```json
{
    "type": "neo-apoli:entities_in_radius",
    "condition": {
        "type": "neo-apoli:is_entity_of_type",
        "entity_type": "minecraft:villager",
        "entity": "entity_in_radius"
    },
    "position": {
        "type": "neo-apoli:entity/position",
        "block": "this"
    },
    "shape": "sphere",
    "radius": 16.0
}
```

This example provides the count of villagers within a 16.0 blocks spherical radius relative to an entity *(provided by the `neo-apoli:this_entity` context parameter.)*


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
