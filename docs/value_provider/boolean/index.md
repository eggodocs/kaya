#   Boolean Provider

Boolean providers are data objects that operate on the given context, and return a boolean value based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired boolean provider.


???+ question "Implict type"

    When defining a boolean provider, if a boolean (`true`/`false`) is specified, it will implicitly use the `constant` boolean provider type.


### List of boolean provider types

- `condition_result`
- `conditional/composite`
- `conditional`
- `constant`
- `nbt`