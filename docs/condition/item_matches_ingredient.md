#   Item Matches Ingredient

Checks if an item matches an ingredient.


Type ID: `neo-apoli:item_matches_ingredient`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`ingredient` | [Ingredient][ingredient] | | The ingredient to match.
`item` | [Item Provider][item_provider] | | The item to check if it matches the ingredient.


### Example

```json
{
    "type": "neo-apoli:item_matches_ingredient",
    "ingredient": "#minecraft:planks",
    "item": "used_item"
}
```

This example will check if the item provided by the `neo-apoli:used_item` context parameter is included in the `#minecraft:planks` item tag.


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
