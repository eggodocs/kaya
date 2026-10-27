#   Modify Model Shaking

Modifies whether the model of the entity holding the power should shake as if it was freezing.


Type ID: `kaya:modify/model/shaking`


### Format

*No additional fields.*


### Example

```json
{
    "type": "kaya:modify/model/shaking",
    "active_condition": {
        "type": "kaya:compare",
        "comparison": {
            "type": "kaya:float",
            "comparator": ">",
            "first": {
                "type": "kaya:round",
                "value": {
                    "type": "kaya:entity/fluid_height",
                    "fluid_tag": "#minecraft:water",
                    "entity": "this"
                },
                "places": 2
            },
            "second": 0.0
        }
    }
}
```

This example will make the model of the entity holding the power shake if it's in water.


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
