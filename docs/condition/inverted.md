#   Inverted

Inverts the result of another condition.


Type ID: `neo-apoli:inverted`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`condition` | [Condition][condition] | | The condition to invert the result of.


### Example

```json
{
    "type": "neo-apoli:inverted",
    "condition": {
        "type": "neo-apoli:is_entity_on_fire",
        "entity": "this"
    }
}
```

This example will check if the entity provided by the `neo-apoli:this_entity` context parameter is **not** on fire.


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
