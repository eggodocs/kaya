#   Constant

Provides a constant NBT value.


Type ID: `neo-apoli:constant`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [NBT]({{ mc.nbt }}) | | The NBT value to provide.


???+ tip

    This type can be inlined by specifying an [NBT]({{ mc.nbt }}).


### Example

=== "Full"

    ```json
    {
        "type": "neo-apoli:constant",
        "value": {
            "Items": [
                {
                    "id": "minecraft:diamond",
                    "count": 1,
                    "Slot": 0
                }
            ]
        }
    }
    ```

=== "Inlined"

    ```json
    {
        "Items": [
            {
                "id": "minecraft:diamond",
                "count": 1,
                "Slot": 0
            }
        ]
    }
    ```


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
