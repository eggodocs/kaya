#   Direction Provider

Direction providers are data objects that operate on the given context, and return a direction based on the provided information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired direction provider type.


???+ question "Implicit type"

    When defining a direction provider, if you specify a [string][string], it will implicitly use the `constant` direction provider type.


### List of types

- `conditional/composite`
- `conditional`
- `constant`
- `opposite`
- `rotate`
