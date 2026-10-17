#   Condition Result

Provides the result of the specified condition.


Type ID: `neo-apoli:condition_result`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to invoke and provide its result of.


### Example

```json
{
    "type": "neo-apoli:condition_result",
    "condition": {
        "type": "neo-apoli:is_entity_sneaking",
        "entity": "this"
    }
}
```

This example provides the result of a condition that checks if the entity provided by the `neo-apoli:this_entity` context parameter is sneaking.


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
