#   Boolean Provider

Boolean providers are data objects that operate on the given context, and return a boolean value based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired boolean provider.


???+ question "Implict type"

    When defining a boolean provider, if a boolean (`true`/`false`) is specified, it will implicitly use the `constant` boolean provider type.


### Meta types

- `conditional/composite`
- `conditional`
- `constant`


### Types

- `condition_result`
- `nbt`
