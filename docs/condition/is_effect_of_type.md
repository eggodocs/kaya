#   Is Effect of Type

Check if a status effect instance is of a specific type.


Type ID: `neo-apoli:is_effect_of_type`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`effect_type` | [Identifier]({{ mc.identifier }}) | | The ID of the status effect type.
`effect` | [Effect Provider][effect_provider] | | The status effect instance to check.


### Example

```json
{
    "type": "neo-apoli:is_effect_of_type",
    "effect_type": "minecraft:poison",
    "effect": "applied_effect"
}
```

This example will check if the type of the status effect instance provided by the `neo-apoli:applied_effect` context parameter is `minecraft:poison`.


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
