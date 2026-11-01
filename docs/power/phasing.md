#   Phasing

Makes the power holder phase through certain blocks.


Type ID: `kaya:phasing`


???+ info

    This type provides the following context parameters when the power holder collides with a block:

    Parameter | Description
    ----------|------------
    `kaya:phased_block` | The block the power holder is about to phase through.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`phase_down_condition` | [Condition][condition] | `{type: "is_entity_sneaking", entity: "this"}` | Determines when the power holder phase through a block below them.
`render_effect` | [Render Effect](#render_effect) | `"blindness"` | Determines the effect to render when the power holder is phasing through blocks.
`view_distance` | [Float][float] | `8.0` | Determines the distance the power holder can see when they're phasing through a block. This value must be at least 2.0.


[](){ #render_effect }

???+ info "Render effect"

    A [string][string] that determines the effect to render when phasing through blocks.

    
    ### Values

    Value | Description
    ------|------------
    `blindness` | Renders a darkened fog around the power holder, as if they have the blindness status effect.
    `none` | Renders no effects.


### Example

```json
{
    "type": "kaya:phasing",
    "phase_down_condition": true,
    "active_condition": {
        "type": "kaya:check_block_type",
        "tag": "#minecraft:impermeable",
        "block": "phased_block"
    }
}
```

This example will make the power holder phase through blocks included in the `#minecraft:impermeable` block tag, such as glass blocks.


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
