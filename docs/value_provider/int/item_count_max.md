#   Item Count Max

Provides the maximum amount of items of an item stack.


Type ID: `kaya:item/count/max`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`item` | [Item Provider][item_provider] | | The item stack to get the maximum amount from.


### Example

```json
{
    "type": "kaya:item/count/max",
    "item": "used_item"
}
```

This example provides the max stack size of the item provided by the `kaya:used_item` context parameter.


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
