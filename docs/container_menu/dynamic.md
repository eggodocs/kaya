#   Dynamic

Provides a container with customizable texture, columns, rows, etc.


Type ID: `kaya:dynamic`


!!! warning

    This type is currently not implemented completely and is not allowed to be used yet.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`title_alignment` | [Text Alignment][text_alignment] | `"center"` | Determines how the title of the menu is aligned.
`texture` | [Identifier]({{ mc.identifier }}) | | The ID of the texture for the menu.
`columns` | [Integer][integer] | | The amount of columns the container would have. The value must be at least 1.
`rows` | [Integer][integer] | | The amount of rows the container would have. The value must be at least 1.


### Example

```json
{
    "type": "kaya:dynamic",
    "texture": "example:awesome_inventory",
    "columns": 16,
    "rows": 16
}
```

This example defines a container with the `example:awesome_inventory` texture, 16 columns, and 16 rows; providing a total of 256 slots.
