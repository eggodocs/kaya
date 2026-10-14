#   Block Provider

Block providers are data objects that operate on the given context, and return a `CachedBlock`(1) based on the provided information.
{ .annotate }


1. `CachedBlock` is a record that contains the provided block's position, state, and entity.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired block provider.


???+ question "Implicit type"

    When defining a block provider, if a [string][string] is specified, it will implicitly use the `context` block provider type.


### List of block provider types

- `conditional/composite`
- `conditional`
- `context`
- `world`