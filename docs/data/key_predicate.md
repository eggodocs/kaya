#   Key Predicate

An object that indicates what ID of a keybinding to check for and if the pressed time of the keybinding is within the specified timing window (if multiple key predicates are defined.)


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`id` | [String Provider][string_provider] | | The ID of the keybinding to check for.
`timing_window` | [Timing Window](#timing_window) | `{min: 3, max: 3}` | The timing window for the keybinding.


???+ tip

    This type can be inlined by specifying a [string][string].


[](){ #timing_window }

???+ info "Timing window"

    An object that indicates the timing window for a pressed keybinding, used for checking the game ticks between multiple pressed keybindings.


    ### Format

    Field | Type | Default | Description
    ------|------|:-------:|------------
    `lower_offset` | [Int Provider][int_provider] | | The amount of additional ticks for the lower bound of the time the keybinding was pressed.
    `upper_offset` | [Int Provider][int_provider] | | The amount of additional ticks for the upper bound of the time the keybinding was pressed.


### Example

=== "Full"

    ```json
    {
        "id": "key.saveToolbarActivator"
    }
    ```

=== "Inlined"

    ```json
    "key.saveToolbarActivator"
    ```
