#   Context

Provides the value of the context parameter from a context.


Type ID: `neo-apoli:context`


!!! note

    This meta type can only provide the same kind of value of the field where it was used. (e.g: if the field is a boolean provider, the context parameter to reference must have a boolean context parameter type, etc.)


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`parameter` | [Identifier]({{ mc.identifier }}) | | The ID of the context parameter. [See here](../../data/context_parameter.md#pre-defined_parameters) for a collection of pre-defined context parameters and their correspondng type.


???+ tip

    This type can be inlined by specifying a [string][string].


### Example

=== "Full"

    ```json
    {
        "type": "neo-apoli:context",
        "parameter": "neo-apoli:this"
    }
    ```

=== "Inlined"

    ```json
    "neo-apoli:this"
    ```

This example is an entity provider that provides the entity provided by the `neo-apoli:this_entity` context parameter.


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

