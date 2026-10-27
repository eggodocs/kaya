#   Revoke All Powers

Revokes all powers from a specified source.


Type ID: `kaya:revoke_all_powers`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`source` | [Identifier]({{ mc.identifier }}) | | The source of the powers to revoke.
`entity` | [Entity Provider][entity_provider] | | The entity to revoke the powers of.


### Example

```json
{
    "type": "kaya:revoke_all_powers",
    "source": "example:epic_stuff",
    "entity": "this"
}
```

This example will revoke all the powers granted with the `example:epic_stuff` source from the entity provided by the `kaya:this_entity` context parameter.


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
