#   Indexed Stack

An object that defines an item stack and its slot in an inventory of an entity/block.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`slot` | [Slot Range]({{ mc.slot_identifier }}) | *optional* | The slot(s) for the item stack.


???+ info

    This type uses the same fields as an item stack. See [Item Stack][item_stack] for the available fields that can be defined.


### Example

```json
{
    "slot": "container.0",
    "id": "minecraft:dirt",
    "count": 3
}
```
