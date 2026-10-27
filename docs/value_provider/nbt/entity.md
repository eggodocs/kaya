#   Entity

Encodes the entity as NBT and uses it as the provided value.


Type ID: `kaya:entity`


???+ info

    See [Minecraft Wiki: Entity format](https://minecraft.wiki/w/Entity_format#Entity_format) for the format when the entity is encoded as NBT.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`entity` | [Entity Provider][entity_provider] | | The entity to encode as NBT.


### Example

```json
{
    "type": "kaya:entity",
    "entity": "this"
}
```

This example encodes the entity provided by the `kaya:this_entity` context parameter and provides it as the NBT value.


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
