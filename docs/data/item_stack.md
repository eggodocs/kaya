#   Item Stack

An object that defines a stack of items.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`id` | [Identifier]({{ mc.identifier }}) | | The ID of the item.
`count` | [Integer][integer] | `1` | The count of the item stack.
`components` | [Components]({{ mc.data_component }}) | *optional* | The data components for the item stack.


### Example

```json
{
    "id": "minecraft:egg",
    "count": 99,
    "components": {
        "minecraft:max_stack_size": 99
    }
}
```

This example defines an Egg item stack with a count of 99 and a max stack size of 99.
