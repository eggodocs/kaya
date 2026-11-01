#   Set Resource Int

Sets the value of a power that uses the [Resource Int](../power/resource_int.md) power type.


Type ID: `kaya:set_resource/int`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] | | The resource power to set the value of.
`entity` | [Entity Provider][entity_provider] | | The entity to get the power from.
`value` | [Int Provider][int_provider] | | The integer value to use.


### Example

```json
{
    "type": "kaya:set_resource/int",
    "power": "example:resource_awesome_sauce",
    "entity": "this",
    "value": {
        "type": "kaya:random/uniform",
        "min": 0,
        "max": 100
    }
}
```

This example will set the value of the `example:resource_awesome_sauce` power from the entity provided by the `kaya:this_entity` context parameter to a random integer value ranging from 0 to 100.


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
