#   Overlay Texture

Overlays a texture sprite on the screen of the player.


Type ID: `kaya:overlay/texture`


!!! tip

    Custom overlay textures must be placed in the `assets/<namespace>/textures/overlay/sprites` directory of a resource pack to be recognized and used properly.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`sprite` | [Sprite][sprite] or [Identifier]({{ mc.identifier }}) | | The sprite definition or ID of the overlay to render. If an ID is specified, it will implicitly use the `kaya:textures/atlas/overlay.png` atlas.
`color` | [Color][color] | *optional* | The color to blend to the colors of the texture sprite. 
`render_phase` | [Render Phase][render_phase] | | Determines when the overlay should be rendered.
`should_render` | [Boolean Provider][boolean_provider] | `true` | Determines whether the overlay should render.
`hide_with_hud` | [Boolean Provider][boolean_provider] | `true` | Determines whether the overlay should hide alongside the HUD. (e.g: when pressing F1)
`visible_in_third_person` | [Boolean Provider][boolean_provider] | `true` | Determines whether the overlay should be visible when in third person.


### Example

```json
{
    "type": "kaya:overlay/texture",
    "sprite": {
        "atlas": "minecraft:textures/atlas/blocks.png",
        "id": "minecraft:block/water_still"
    },
    "color": {
        "type": "kaya:biome/water",
        "position": {
            "type": "kaya:entity/position",
            "entity": "this"
        },
        "alpha": 0.50
    },
    "render_phase": "below_hud"
}
```

This example renders a translucent water overlay with its color being dependent on the water color of the biome the entity is currently in.


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
