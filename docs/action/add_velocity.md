#   Add Velocity

Adds velocity to an entity.


Type ID: `neo-apoli:add_velocity`


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`method` | [Method](#method) | | Determines the method of adding velocity to an entity.
`velocity` | [Vec3 Provider][vec3_provider] | | The velocity to add to the entity.


[](){ #method }

???+ info "Method"

    A [string][string] that determines how velocity is applied to an entity. Each type has additional fields to further control how the velocity is applied.

    === "`single`"

        Field | Type | Default | Description
        ------|------|:-------:|------------
        `space` | [Space][space] | `"world"` | Determines how the velocity will be transformed.
        `entity` | [Entity Provider][entity_provider] | | The entity to add the velocity to.

    === "`pair`"

        Field | Type | Default | Description
        ------|------|:-------:|------------
        `reference` | [Reference](#reference) | `"rotation"` | Determines the direction of the velocity is calculated from the two entities.
        `first` | [Entity Provider][entity_provider] | | The entity to use as a reference.
        `second` | [Entity Provider][entity_provider] | | The entity to add the velocity to.


        [](){ #reference }

        ??? info "Reference"

            A [string][string] that determines how the velocity will be transformed based on two entities.


            ### Values

            Value | Description
            ------|------------
            `position` | Use the positions of the first and second entities to transform the velocity.
            `rotation` | Use the rotation of the first entity to transform the velocity.


### Example

=== "Single"

    ```json
    {
        "type": "neo-apoli:add_velocity",
        "method": "single",
        "space": "world",
        "entity": "this",
        "velocity": [
            0.0,
            10.0,
            0.0
        ]
    }
    ```

    This example will launch the entity from the `neo-apoli:this_entity` context parameter high in the air.

=== "Pair"

    ```json
    {
        "type": "neo-apoli:add_velocity",
        "method": "pair",
        "reference": "rotation",
        "first": "actor",
        "second": "target",
        "velocity": [
            0.0,
            0.0,
            -2.0
        ]
    }
    ```

    This example will essentially pull the entity from the `neo-apoli:target_entity` context parameter to the entity from the `neo-apoli:actor_entity` context parameter.


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
        <td style="vertical-align: middle">Added the power type.</td>
    </tr>
</table>
