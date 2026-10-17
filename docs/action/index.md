#   Action

Actions are used to operate on a given context. Actions can change or affect the world and/or its entities depending on the specified type.

Custom actions can be defined as JSON/JSON5/JSONC files in the `data/<namespace>/neo-apoli/action` directory of a data pack. Data packs that load later with an action file with the same name and directory will replace the existing action.


!!! note

    Some actions require certain context parameters to function properly. Make sure to check the page for the desired action type for more information.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Identifier]({{ mc.identifier }}) | | The identifier of the desired action type.


???+ tip

    Specifying certain data types will implicitly use a specific type:

    Data Type | Action Type
    ----------|------------
    [Array][array] of [Actions][action] | [`sequence`](sequence.md)
    Empty Object (`{}`) | [`nothing`](nothing.md)


### Meta types

-   [`conditional/composite`](conditional_composite.md)
-   [`conditional`](conditional.md)
-   [`loop`](loop.md)
-   [`nothing`](nothing.md)
-   [`reference`](reference.md)
-   [`sequence`](sequence.md)
-   [`side`](side.md)
-   [`weighted`](weighted.md)


### Types

-   [`add_velocity`](add_velocity.md)
-   [`apply_effects`](apply_effects.md)
-   `area_of_effect`
-   `bone_meal`
-   `clear_powers`
-   `consume_item`
-   `damage_entity`
-   `damage_item`
-   `dismount`
-   `emit_game_event`
-   `execute_command`
-   `exhaust`
-   `explode`
-   `extinguish_entity_fire`
-   `gain_air`
-   `give_items`
-   `grant_power`
-   `modify_block_state_property`
-   `modify_item`
-   `mount`
-   `place_block`
-   `play_sound`
-   `random_chance`
-   `remove_power`
-   `revoke_all_powers`
-   `revoke_power`
-   `set_entity_on_fire`
-   `shoot_entity`
-   `side`
-   `spawn_particles`
-   `swing_hand`
-   `tame`
-   `toggle_power`
-   `trigger_power_cooldown`
