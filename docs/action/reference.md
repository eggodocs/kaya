#   Reference

Invokes a condition file and returns its value.


Type ID: `neo-apoli:reference`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Identifier]({{ mc.identifier }}) | | The ID of the condition to invoke.
`parameters` | [Context Parameter Map][context_parameter_map] | *optional* | If specified, these context parameters will be provided to the context for invoking the condition.


### Example

=== "Simple"

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


=== "Complex"

    ```json
    {
        "type": "neo-apoli:reference",
        "value": "example:item/is_armor_higher_than_threshold"/*(1)!*/,
        "parameters": {
            "example:item": {
                "type": "neo-apoli:item",
                "value": "worn_item"
            },
            "example:threshold": {
                "type": "neo-apoli:float",
                "value": 2.0
            }
        }
    }
    ```

    1. The location of the file is `data/example/neo-apoli/condition/item/is_armor_higher_than_threshold.json` with this as its contents:
   
        ```json
        {
            "type": "neo-apoli:compare",
            "comparison": {
                "type": "neo-apoli:float",
                "comparator": ">",
                "first": {
                    "type": "neo-apoli:item/attribute",
                    "attribute": "minecraft:armor",
                    "item": "example:item"
                },
                "second": "example:threshold"
            }
        }
        ```

    This example provides the context parameters (specifically used by the condition) before invoking the `example:item/is_armor_higher_than_threshold` condition.


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
