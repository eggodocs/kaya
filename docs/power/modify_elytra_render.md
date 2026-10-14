#   Modify Elytra Render

Modifies how an elytra wings is rendered on the entity holding the power.


Type ID: `neo-apoli:modify/elytra/render`


!!! note

    When rendering the elytra wings, this power type will specifically use the `wings` layer defined in the equipment definition specified in `asset_id`. See [Minecraft Wiki: Equipment](https://minecraft.wiki/w/Equipment) for more information about creating custom equipment definitions.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`asset_id` | [Identifier]({{ mc.identifier }}) | | The ID of the equipment definition to use.
`trim` | [Identifier]({{ mc.identifier }}) | *optional* | If specified, the trim with this ID will be applied to the rendered wings.
`color` | [Color][color] | *optional* | If specified, this color will be applied to the rendered wings.
`priority` | [Integer][integer] | `0` | Determines the order of which the powers are iterated.


??? question "About priorities"

    The instances of this type will be sorted in its **reversed** *natural order* meaning that instances that have a higher priority value will have its elytra wings rendered first before those that have a lower priority value.


### Example

```json
{
    "type": "neo-apoli:modify/elytra/render",
    "asset_id": "example:dyeable_elytra", // (1)!
    "color": {
        "type": "neo-apoli:biome/foliage",
        "position": {
            "type": "neo-apoli:entity/position",
            "entity": "this"
        },
        "alpha": 1.0,
        "dry": false
    }
}
```

1. The file is `assets/example/equipment/dyeable_elytra.json` with this being its contents:

    ```json
    {
        "layers": {
            //  For the elytra to be rendered, the properties must be defined in the 'wings' layer!
            "wings": [
                {
                    "texture": "minecraft:elytra",
                    "use_player_texture": true,
                    "dyeable": {}
                }
            ]
        }
    }
    ```

This example renders an elytra wings to the entity holding the power with its color being dependent on the biome the entity is in.


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
