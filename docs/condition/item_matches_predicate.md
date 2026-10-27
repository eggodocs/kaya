#   Item Matches Predicate

Checks if an item matches an item predicate argument.


Type ID: `kaya:item_matches_predicate`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`predicate` | [Item Predicate Argument]({{ mc.item_predicate_argument }}) | | The item predicate argument to match.
`item` | [Item Provider][item_provider] | | The item to check if it matches the item predicate argument.


### Example

```json
{
    "type": "kaya:item_matches_predicate",
    "predicate": "*[minecraft:food]",
    "item": "item_in_container"
}
```

This example will check if the item provided by the `kaya:item_in_container` context parameter has the `minecraft:food` item component.


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
