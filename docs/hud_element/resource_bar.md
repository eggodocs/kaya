#   Resource Bar

Renders a bar above the hunger status bar on the HUD.


Type ID: `kaya:resource_bar`


!!! tip

    Custom resource bar textures must be placed in the `assets/<namespace>/textures/gui/sprites` directory of a resource pack to be recognized and used properly. [See here](https://github.com/eggomods/kaya/tree/1.21.5/src/client/resources/assets/kaya/textures/gui/sprites/resource_bar) for a collection of resource bar sprites included in the mod.


???+ info

    This HUD element type uses the following context parameters. The following fields must, or must not be present, depending on whether the context parameters are provided:

    Parameter | Field
    ----------|------
    `kaya:hud/value` | `value`
    `kaya:hud/max_value` | `max`
    `kaya:hud/min_value` | `min`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`sprite_location` | [Sprite Location](#sprite_location) | *optional* | The IDs of the bar sprites to render.
`inverted` | [Boolean Provider][boolean_provider] | `false` | Determines whether the bar should progress from left-to-right or right-to-left.
`x` | [Int Provider][int_provider] | `0` | Determines the offset position of the bar on the horizontal axis.
`y` | [Int Provider][int_provider] | `0` | Determines the offset position of the bar on the vertical axis.
`should_render` | [Boolean Provider][boolean_provider] | `true` | Determines whether the bar should be rendered. 
`value` | [Float Provider][float_provider] | *optional* | If present, this will be used as the "fill" value of the bar.
`min` | [Float Provider][float_provider] | *optional* | If present, this will be used as the minimum bounds of the bar.
`max` | [Float Provider][float_provider] | *optional* | If present, this will be used as the maximum bounds of the bar.


[](){ #sprite_location }

???+ info "Sprite Location"

    The `sprite_location` has the following format:

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `background` | [Identifier]({{ mc.identifier }}) | `"kaya:resource_bar/1/background"` | The ID of bar's background texture.
    `fill` | [Identifier]({{ mc.identifier }}) | `"kaya:resource_bar/1/fill"` | The ID of the bar's "fill" portion texture.
    `icon` | [Identifier]({{ mc.identifier }}) | `"kaya:resource_bar/1/icon"` | The ID of the bar's icon, rendered on the left side of the bar.


### Example

```json
{
    "type": "kaya:resource_bar",
    "sprite_location": {
        "background": "kaya:resource_bar/1/background"/*(1)!*/,
        "fill": "kaya:resource_bar/9/fill"/*(2)!*/,
        "icon": "kaya:resource_bar/2/icon"/*(3)!*/
    },
    "render_phase": "below_hud"
}
```

This example renders a resource bar differing textures; where it uses the background sprite of the 1st resource bar, the fill sprite of the 9th resource bar, and the icon sprite of the 2nd resource bar. (All referenced resource bars in the example are included in the mod.)


1. The image: ![Image](https://raw.githubusercontent.com/eggomods/kaya/refs/heads/1.21.5/src/client/resources/assets/kaya/textures/gui/sprites/resource_bar/1/background.png)
2. The image: ![Image](https://raw.githubusercontent.com/eggomods/kaya/refs/heads/1.21.5/src/client/resources/assets/kaya/textures/gui/sprites/resource_bar/9/fill.png)
3. The image: ![Image](https://raw.githubusercontent.com/eggomods/kaya/refs/heads/1.21.5/src/client/resources/assets/kaya/textures/gui/sprites/resource_bar/2/icon.png)


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
