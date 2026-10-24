#   Provide Context

Invokes a condition with the provided context parameters.


Type ID: `neo-apoli:provide_context`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to invoke.
`parameters` | [Context Parameter Map][context_parameter_map] | | The context parameters to provide.


### Example

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

This example will invoke the `example:item/is_armor_higher_than_threshold` condition, provide the context parameters that it uses, and uses its result.


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
