#   Grant Power

Grants a power or a collection of powers to an entity.


Type ID: `kaya:grant_power`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`power` | [Power Identifier][power_identifier] or [Power Tag]({{ mc.tag }}) | | The ID or tag of the power(s) to grant.
`source` | [Identifier]({{ mc.identifier }}) | | Indicates where the power is from.
`entity` | [Entity Provider][entity_provider] | | The entity to grant the power(s) to.


### Example

```json
{
    "type": "kaya:grant_power",
    "power": "#example:all_the_good_stuff"/*(1)!*/,
    "source": "example:epic_stuff",
    "entity": "this"
}
```


1. The location of the file is `data/example/tags/kaya/power/all_the_good_stuff.json`


This example will grant all the powers included in the `#example:all_the_good_stuff` power tag to the entity provided by the `kaya:this_entity` context parameter with the source `example:epic_stuff`.


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
