#   Box

Defines an area that's based from the provided box.


Type: `neo-apoli:box`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`box` | [Box Provider][box_provider] | | The box to use as the area.


### Example

```json
{
    "type": "neo-apoli:box",
    "target": "block",
    "shape": "sphere",
    "box": {
        "type": "neo-apoli:inflate",
        "box": {
            "type": "neo-apoli:entity/bounds",
            "entity": "this"
        },
        "vector": [
            4.0,
            4.0,
            4.0
        ]
    }
}
```

This example will provide an area based on the bounding box of the entity provided by the `neo-apoli:this_entity` context parameter (inflated by 4 blocks in all directions) that will only target blocks.


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
