#   Reference

Invokes a condition file and returns its value.


Type ID: `neo-apoli:reference`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Identifier]({{ mc.identifier }}) | | The ID of the condition to invoke.


### Example

```json
{
    "type": "neo-apoli:reference",
    "value": "example:entity/is_in_water"//(1)!
}
```

1. The location of the file is `data/example/neo-apoli/condition/entity/is_in_water.json` with this as its contents:

    ```json
    {
        "type": "neo-apoli:compare",
        "comparison": {
            "type": "neo-apoli:float",
            "comparator": ">",
            "first": {
                "type": "neo-apoli:entity/fluid_height",
                "fluid_tag": "#minecraft:water",
                "entity": "this"
            },
            "second": 0.0
        }
    }
    ```

This example invokes the `example:entity/is_in_water` condition and returns its result.


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
