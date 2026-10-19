#   Max

Gets the highest number from all the number values and uses it as the provided number value.


Type ID: `neo-apoli:max`


!!! note
    
    This number meta type can only provide the same kind of value of the field where it was used. *(e.g: if the field is a float provider, the number provider to specify should be a float provider or if the field is an int provider, the number provider to specify should be an int provider)*


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`values` | [Array][array] of [Number Providers][number_providers] | | The numbers to get the highest number from.


### Example

```json
{
    "type": "neo-apoli:max",
    "values": [
        {
            "type": "neo-apoli:player/food",
            "entity": "this"
        },
        1
    ]
}
```

This example is an int provider that will get the highest integer between the food level of the player provided by the `neo-apoli:this_entity` context parameter and $1$.


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
