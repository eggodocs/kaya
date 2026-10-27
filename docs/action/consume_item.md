#   Consume Item

Reduces the count of an item.


Type ID: `kaya:consume_item`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`amount` | [Int Provider][int_provider] | `1` | The amount to subtract from the item's count.
`slot` | [Slot Provider][slot_provider] | | The slot of the item to consume.


### Example

```json
{
    "type": "kaya:consume_item",
    "slot": {
        "type": "kaya:entity",
        "entity": "this",
        "slot": {
            "type": "kaya:slot_id",
            "slot": "hotbar.0"
        }
    }
}
```

This example will consume the item from the first hotbar slot of the entity provided by the `kaya:this_entity` context parameter.


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
