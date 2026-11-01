#   Set Resource Float

Sets the value of a power that uses the [Resource Float](../power/resource_float.md) power type.


Type ID: `kaya:set_resource/float`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The resource power to set the value of.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.
`value` | [Float Provider][float_provider] | | The float value to use.


### Example

```json
{
    "type": "kaya:set_resource/float",
    "power": "example:resource_awesome_sauce_but_as_float",
    "entity": "this",
    "value": {
        "type": "kaya:product",
        "values": [
            {
                "type": "kaya:entity/attribute",
                "attribute": "minecraft:armor",
                "entity": "this"
            },
            0.01
        ]
    }
}
```

This example will set the value of the `example:resource_awesome_sauce_but_float` power from the entity provided by the `kaya:this_entity` context parameter to the value of its `minecraft:armor` attribute multiplied by 0.01.


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
