#   Quotient

Divides a number and uses the quotient as the provided number value.


Type ID: `neo-apoli:quotient`


!!! note
    
    This number meta type can only provide the same kind of value of the field where it was used. *(e.g: if the field is a float provider, the number provider to specify should be a float provider or if the field is an int provider, the number provider to specify should be an int provider)*


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`dividend` | Number Provider | | The number to divide.
`divisor` | Number Provider | | The number used to divide the dividend.


### Example

```json
{
    "type": "neo-apoli:quotient",
    "dividend": {
        "type": "neo-apoli:from_int",
        "value": {
            "type": "neo-apoli:player/food",
            "entity": "this"
        }
    },
    "divisor": 20
}
```

This example is a float provider that will divide the food level of the player provided by the `neo-apoli:this_entity` context parameter by $20$ and provides it as the value.

$(Value = FoodLevel \div 20)$


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
