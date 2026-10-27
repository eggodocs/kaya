#   Box Component

Provides the component (min/max values) of a box from a specific side.


Type ID: `kaya:box/component`


??? info "Box components and sides"

    Each direction returns a specific component of a box:

    Direction | Component
    ----------|----------
    `down` | The minimum Y component of the box.
    `up` | The maximum Y component of the box.
    `north` | The minimum Z component of the box.
    `south` | The maximum Z component of the box.
    `west` | The minimum X component of the box.
    `east` | The maximum X component of the box.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`box` | [Box Provider][box_provider] | | The box to get its component of.
`side` | [Direction Provider][direction_provider] | | The side of the box to get the component from.


### Example

```json
{
    "type": "kaya:box/component",
    "box": {
        "type": "kaya:entity/bounds",
        "entity": "this"
    },
    "side": "up"
}
```

This example provides the maximum Y component of the bounding box of the entity *(provided by the `kaya:this_entity` context parameter.)*


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
