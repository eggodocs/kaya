#   Resize

Resizes a box by adding the minimum and maximum bounds of another box.


Type ID: `neo-apoli:resize`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`box` | [Box Provider][box_provider] | | The box to resize.
`offset` | [Box Provider][box_provider] | | The other box to use for resizing the box.


### Example

```json
{
    "type": "neo-apoli:offset",
    "box": {
        "type": "neo-apoli:entity/bounds",
        "entity": "this"
    },
    "offset": [
        0.0,
        0.0,
        0.0,
        1.0,
        1.0,
        1.0
    ]
}
```

This example provides the bounding box of the entity provided by the `neo-apoli:this_entity` context parameter and expands it towards the positive X, Y, and Z axes by 1 block.


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
