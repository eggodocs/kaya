#   Modify Item

Applies an item modifier to an item stack.


Type ID: `kaya:modify_item`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`modifier` | [Identifier]({{ mc.identifier }}) | | The ID of the item modifier.
`slot` | [Slot Provider][slot_provider] | | The slot of the item that will be modified.
`position` | [Vec3 Provider][vec3_provider] | *optional* | If specified, this position will be passed as the `minecraft:origin` vanilla context parameter for the item modifier.
`entity` | [Entity Provider][entity_provider] | *optional* | If specified, this entity will be used as the `minecraft:this_entity` vanilla context parameter for the item modifier.


### Example

```json
{
    "type": "kaya:modify_item",
    "modifier": "example:smelt_item"/*(1)!*/,
    "slot": "used_item_slot"
}
```


1. The location of the file is `data/example/item_modifier/smelt_item.json` with the following as its contents:

    ```json
    {
        "function": "minecraft:furnace_smelt"
    }
    ```


This example will essentially smelt the item provided by the `kaya:used_item_slot` context parameter.


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
