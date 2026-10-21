#   Command Source Provider

Command source providers are data objects that operate on the given context, and return a `CommandSourceStack`(1) based on the provided information.
{ .annotate }


1. `CommandSourceStack` is vanilla's object used for executing commands.


???+ warning

    Command source providers are strictly **server-sided** only.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired command source provider.


???+ tip

    Specifying a [string][string] will implicitly use one of the following types that match:

    - [`server`](server.md)


### Meta types

- [`conditional/composite`](../meta/conditional_composite.md)
- [`conditional`](../meta/conditional.md)
- [`weighted`](../meta/weighted.md)


### Types

- [`block`](block.md)
- [`entity`](entity.md)
- [`server`](server.md)
