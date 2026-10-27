#   Product

Multiplies all the number values and uses the product as the provided number value.


Type ID: `kaya:product`


!!! note
    
    This number meta type can only provide the same kind of value of the field where it was used. *(e.g: if the field is a float provider, the number provider to specify should be a float provider or if the field is an int provider, the number provider to specify should be an int provider)*


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`values` | [Array][array] of Number Providers | | The numbers to get the product of.


### Example

```json
{
    "type": "kaya:difference",
    "values": [
        {
            "type": "kaya:entity/attribute",
            "attribute": "minecraft:armor",
            "entity": "this"
        },
        0.1
    ]
}
```

This example is a float provider that would multiply the value of the `minecraft:armor` attribute of the entity provided by the `kaya:this_entity` context parameter by $0.1$.

$(Value = AttributeValue * 0.1)$


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
