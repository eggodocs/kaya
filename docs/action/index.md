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

- [`conditional/composite`](conditional_composite.md)
- [`conditional`](conditional.md)
- [`loop`](loop.md)
- [`nothing`](nothing.md)
- [`random_chance`](random_chance.md)
- [`reference`](reference.md)
- [`sequence`](sequence.md)
- [`side`](side.md)
- [`weighted`](weighted.md)


### Types

- [`add_velocity`](add_velocity.md)
- [`apply_effects`](apply_effects.md)
- [`area_of_effect`](area_of_effect.md)
- [`bone_meal`](bone_meal.md)
- [`clear_powers`](clear_powers.md)
- [`consume_item`](consume_item.md)
- [`damage_entity`](damage_entity.md)
- [`damage_item`](damage_item.md)
- [`dismount`](dismount.md)
- [`emit_game_event`](emit_game_event.md)
- [`execute_command`](execute_command.md)
- [`exhaust`](exhaust.md)
- [`explode`](explode.md)
- [`extinguish_entity_fire`](extinguish_entity_fire.md)
- [`gain_air`](gain_air.md)
- [`give_items`](give_items.md)
- [`grant_power`](grant_power.md)
- [`modify_block_state_property`](modify_block_state_property.md)
- [`modify_item`](modify_item.md)
- [`mount`](mount.md)
- [`place_block`](place_block.md)
- [`play_sound`](play_sound.md)
- [`remove_power`](remove_power.md)
- [`revoke_all_powers`](revoke_all_powers.md)
- [`revoke_power`](revoke_power.md)
- [`set_entity_on_fire`](set_entity_on_fire.md)
- [`shoot_entity`](shoot_entity.md)
- [`spawn_particles`](spawn_particles.md)
- [`swing_hand`](swing_hand.md)
- [`tame`](tame.md)
- [`toggle_power`](toggle_power.md)
- [`trigger_power_cooldown`](trigger_power_cooldown.md)
