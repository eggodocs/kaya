#   Revoke Power

Revokes a power or a collection of powers from an entity.


Type ID: `neo-apoli:revoke_power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] or [Power Tag]({{ mc.tag }}) | | The ID or tag of the power(s) to revoke.
`source` | [Identifier]({{ mc.identifier }}) | | The source of the power(s) to revoke.
`entity` | [Entity Provider][entity_provider] | | The entity to revoke the power(s) of.


### Example

```json
{
    "type": "neo-apoli:grant_power",
    "power": "#example:all_the_good_stuff"/*(1)!*/,
    "source": "example:epic_stuff",
    "entity": "this"
}
```


1. The location of the file is `data/example/tags/neo-apoli/power/all_the_good_stuff.json`


This example will revoke all the powers included in the `#example:all_the_good_stuff` power tag from the entity provided by the `neo-apoli:this_entity` context parameter granted with the source `example:epic_stuff`.


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
