#   Item Fuel

Provides the fuel value of an item stack *(in ticks.)*


Type ID: `kaya:item/fuel`


???+ tip

    See [Minecraft Wiki: Smelting (Fuel)](https://minecraft.wiki/w/Smelting#Fuel) for a table of items and their fuel values.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`item` | [Item Provider][item_provider] | | The item to get its fuel value of.


### Example

```json
{
    "type": "kaya:item/fuel",
    "item": "used_item"
}
```

This example provides the fuel value of the item stack provided by the `kaya:used_item` context parameter. For example, if the item is a coal, the provided value will be $1600$.


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
