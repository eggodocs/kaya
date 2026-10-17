#   Item

Encodes the item as NBT and uses it as the provided value.


Type ID: `neo-apoli:item`


???+ info

    See [Minecraft Wiki: Data component format (Item format)](https://minecraft.wiki/w/Data_component_format#Item_format) for the format when the item is encoded as NBT.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`item` | [Item Provider][item_provider] | | The item to encode as NBT.


### Example

```json
{
    "type": "neo-apoli:item",
    "item": "used_item"
}
```

This example encodes the item provided by the `neo-apoli:used_item` context parameter and uses it as the provided value.


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
