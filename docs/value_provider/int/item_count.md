#   Item Count

Provides how many items are in an item stack.


Type ID: `kaya:item/count`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`item` | [Item Provider][item_provider] | | The item stack to get the amount of items of.


### Example

```json
{
    "type": "kaya:item/count",
    "item": "item_in_container"
}
```

This example provides the amount of items of the item stack provided by the `kaya:item_in_container` context parameter.


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
