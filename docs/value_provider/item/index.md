#   Item Provider

Item providers are data objects that operate on the given context, and return an item stack based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type`| [Identifier]({{ mc.identifier }}) | | The identifier of the desired item provider type.


???+ tip

    Specifying a [string][string] will implicitly use the `context` item provider type.


### Types

- `conditional/composite`
- `conditional`
- `context`
