#   NBT

Compares the elements (and its contents, if it's a list) of the first and second NBTs.


Type ID: `neo-apoli:nbt`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`first` | [NBT Provider][nbt_provider] | | The first NBT to compare to.
`second` | [NBT Provider][nbt_provider] | | The second NBT to be compared.


### Example

```json
{
    "type": "neo-apoli:nbt",
    "first": {
        "Item": {
            "components": {
                "minecraft:custom_data": {
                    "example:data": {
                        "striker": true
                    }
                }
            }
        }
    },
    "second": {
        "type": "neo-apoli:entity",
        "entity": "projectile"
    }
}
```

This example compares the NBT of the entity from the `neo-apoli:projectile_entity` context parameter to the first NBT, essentially checking if the entity has an item that has the `minecraft:custom_data` item component that contains an `example:data` NBT compound with `striker: 1b`.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
