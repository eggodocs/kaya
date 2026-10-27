#   Box Size

Provides the size of a box.


Type ID: `kaya:box/size`


???+ info

    The size of the box is calculated by the following formula: $(Size = ((Max_x - Min_x) + (Max_y - Min_y) + (Max_z - Min_z)) \div 3.0)$


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`box` | [Box Provider][box_provider] | | The box to get the size of.


### Example

```json
{
    "type": "kaya:box/size",
    "box": {
        "type": "kaya:entity/bounds",
        "entity": "projectile"
    }
}
```

This example provides the size of the bounding box from the entity *(provided by the `kaya:projectile_entity` context parameter.)*


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
