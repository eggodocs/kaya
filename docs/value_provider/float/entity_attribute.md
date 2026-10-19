#   Entity Attribute

Provides the value of an attribute from an entity.


Type ID: `neo-apoli:entity/attribute`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`attribute` | [Identifier]({{ mc.identifier }}) | | The ID of the attribute.
`entity` | [Entity Provider][entity_provider] | | The entity to get the attribute from.


### Example

```json
{
    "type": "neo-apoli:entity/attribute",
    "attribute": "minecraft:max_health",
    "entity": "actor"
}
```

This example will provide the value of the `minecraft:max_health` attribute from an entity *(provided by the `neo-apoli:actor_entity` context parameter.)*


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
