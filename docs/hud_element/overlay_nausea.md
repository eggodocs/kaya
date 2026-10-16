#   Overlay Nausea

Overlays a texture sprite on the screen of the player, with the alpha component of the color being the intensity of the color and stretch factor of the texture.


Type ID: `neo-apoli:overlay/nausea`


!!! note

    This HUD element type blends the colors to the texture additively. It also treats black pixels in the texture as transparent.


!!! tip

    Custom overlay textures must be placed in the `assets/<namespace>/textures/overlay/sprites` directory of a resource pack to be recognized and used properly.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`sprite` | [Sprite][sprite] or [Identifier]({{ mc.identifier }}) | | The sprite definition or ID of the overlay to render. If an ID is specified, it will implicitly use the `neo-apoli:textures/atlas/overlay.png` atlas.
`color` | [Color][color] | *optional* | The color to blend to the colors of the texture sprite. 
`render_phase` | [Render Phase][render_phase] | | Determines when the overlay should be rendered.
`should_render` | [Boolean Provider][boolean_provider] | `true` | Determines whether the overlay should render.
`hide_with_hud` | [Boolean Provider][boolean_provider] | `true` | Determines whether the overlay should hide alongside the HUD. (e.g: when pressing F1)
`visible_in_third_person` | [Boolean Provider][boolean_provider] | `true` | Determines whether the overlay should be visible when in third person.
`order` | [Integer][integer] | `0` | Determines the order of which the overlay is rendered over other HUD elements.


??? question "About orders"

    HUD elements will be sorted in its *natural order* meaning that HUD elements that have a lower order value will be rendered first before those that have a higher order values.


### Example

```json
{
    "type": "neo-apoli:overlay/nausea",
    "sprite": "example:nausea_overlay"/*(1)!*/,
    "color": "#32c5ff9d",
    "render_phase": "below_hud",
    "hide_with_hud": false
}
```

This example renders a light blue and slightly transparent overlay that doesn't hide when the HUD is hidden.


1. The location for the texture file in a resource pack is `assets/example/textures/overlay/sprites/nausea_overlay.png`


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
