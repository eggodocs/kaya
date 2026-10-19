#   Clamped

Provides the number value clamped to a specific minimum and maximum range.


Type ID: `neo-apoli:clamped`


!!! note
    
    This number meta type can only provide the same kind of value of the field where it was used. *(e.g: if the field is a float provider, the number provider to specify should be a float provider or if the field is an int provider, the number provider to specify should be an int provider)*


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`value` | [Number Provider][number_providers] | | The number value to provide and clamp.
`min` | [Number Provider][number_providers] | | The minimum number value for the provided number value.
`max` | [Number Provider][number_providers] | | The maximum number value for the provided number value.


### Example

```json
{
    "type": "neo-apoli:clamped",
    "value": {
        "type": "neo-apoli:entity/attribute",
        "attribute": "minecraft:max_health",
        "entity": "this"
    },
    "min": 1.0,
    "max": 20.0
}
```

This example is a float provider that provides the value of the `minecraft:max_health` attribute of the entity provided by the `neo-apoli:this_entity` context parameter. The float value is then clamped where its value will be within the range of $1.0$ to $20.0$.


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
