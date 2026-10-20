#   Key Pressed Time

Provides the time the key was pressed *(in ticks.)*


Type ID: `neo-apoli:key/pressed/time`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`id` | [String Provider][string_provider] | | The ID of the keybinding.
`entity` | [Entity Provider][entity_provider] | | The entity to get the state of the keybinding from.


### Example

```json
{
    "type": "neo-apoli:key/pressed/time",
    "id": "key.forward",
    "entity": "this"
}
```

This example will provide the game ticks the `key.forward` keybinding was pressed by the entity provided by the `neo-apoli:this_entity` context parameter.


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
