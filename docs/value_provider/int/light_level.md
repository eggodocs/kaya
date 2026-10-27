#   Light Level

Provides the light level at a position.


Type ID: `kaya:light_level`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`light_type` | [Light Type](#light_type) | *optional* | Determines the type of light which level will be provided.
`position` | [Vec3 Provider][vec3_provider] | | The position to get the light level from.


[](){ #light_type }

??? info "Light type"

    A [string][string] that indicates where the light came from.

    
    {% if light_types %}

    ### Values

    Value | Description
    ------|------------
    {%- for light_type in light_types %}
    `{{ light_type.name }}` | {{ light_type.description }}
    {%- endfor %}
    {% endif %}


???+ info

    If `light_type` is not specified, the highest light level between the block light level and **internal** sky light level will be provided.

    See [Minecraft Wiki: Light (Internal light level)](https://minecraft.wiki/w/Light#Internal_light_level) for more information about internal sky light levels.


### Example

```json
{
    "type": "kaya:light_level",
    "light_type": "sky",
    "position": {
        "type": "kaya:offset",
        "vector": {
            "type": "kaya:block/position",
            "block": "used_block"
        },
        "offset": [
            0.0,
            1.0,
            0.0
        ]
    }
}
```

This example will provide the sky light level relative to the position of the block provided by the `kaya:used_block` context parameter, offset by 1 block up.


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
