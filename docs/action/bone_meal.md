#   Bone Meal

Applies bone meal to blocks on a position.


Type ID: `neo-apoli:bone_meal`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`position` | [Vec3 Provider][vec3_provider] | | The position to apply a bone meal to.
`show_effects` | [Boolean Provider][boolean_provider] | `true` | Determines whether to show the particle effects when bone meal is applied.
`offset_direction` | [Direction Provider][direction_provider] | *optional* | If specified, bone meal will be applied to the block at the position offset by this direction if the initial bone meal application failed.


### Example

```json
{
    "type": "neo-apoli:bone_meal",
    "position": {
        "type": "neo-apoli:block/position",
        "block": "used_block"
    },
    "offset_direction": {
        "type": "neo-apoli:context",
        "parameter": "used_side"
    }
}
```

This example will attempt to apply bone meal to the block provided by the `neo-apoli:used_block` context parameter. If it fails, it will apply the bone meal at the block offset by the direction provided by the `neo-apoli:used_side` context parameter instead.


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
