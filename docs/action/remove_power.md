#   Remove Power

Removes a power or a collection of powers from an entity.


Type ID: `kaya:remove_power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] or [Power Tag]({{ mc.tag }}) | | The ID or tag of the power(s) to remove.
`entity` | [Entity Provider][entity_provider] | | The entity to remove the power(s) from.


### Example

```json
{
    "type": "kaya:remove_power",
    "power": "#example:bad_stuff"/*(1)!*/,
    "entity": "this"
}
```


1. The location of the file is `data/example/tags/kaya/power/bad_stuff.json`


This example will remove all the powers included in the `#example:bad_stuff` power tag from the entity provided by the `kaya:this_entity` context parameter.


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
