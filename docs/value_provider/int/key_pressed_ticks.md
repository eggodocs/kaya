#   Key Pressed Ticks

Provides how long a keybinding has been pressed/held *(in ticks.)*


Type ID: `kaya:key/pressed/ticks`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`id` | [String Provider][string_provider] | | The ID of the keybinding.
`entity` | [Entity Provider][entity_provider] | | The entity to get the state of the keybinding from.


### Example

```json
{
    "type": "kaya:key/pressed/ticks",
    "id": "key.use",
    "entity": "this"
}
```

This example will provide how long the `key.use` keybinding has been pressed/held for by the entity provided by the `kaya:this_entity` context parameter.


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
