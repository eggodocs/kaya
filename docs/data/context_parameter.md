#   Context Parameter

An object that determines a parameter, which indicates what kind of object is stored in a context.


??? tip "Pre-defined parameters"

    In neo-apoli, there are pre-defined context parameters that are used/shared by certain types:

    Parameter | Type |Description
    ----------|------|-----------
    `neo-apoli:command/entity` | `neo-apoli:entity` | Refers to the entity that executed the command.
    `neo-apoli:command/position` | `neo-apoli:vec3` | Refers to the position of the executed command.
    `neo-apoli:actor_entity` | `neo-apoli:entity` | Usually refers to an entity that did an action. (e.g: the attacker)
    `neo-apoli:target_entity` | `neo-apoli:entity` | Usually refers to the entity that was targeted. (e.g: the victim)
    `neo-apoli:projectile_entity` | `neo-apoli:entity` | Refers to a projectile entity.
    `neo-apoli:this_entity` | `neo-apoli:entity` | Usually refers to the entity holding a power.
    `neo-apoli:dealt_damage/source` | `neo-apoli:damage_source` | The damage source dealt by an entity.
    `neo-apoli:taken_damage/source` | `neo-apoli:damage_source` | The damage source taken by an entity.
    `neo-apoli:dealt_damage/amount` | `neo-apoli:float` | The amount of damage dealt to an entity.
    `neo-apoli:taken_damage/amount` | `neo-apoli:float` | The amount of damage taken by an entity.
    `neo-apoli:damaging_entity` | `neo-apoli:entity` | The projectile used for the attack (or the attacker entity if no projectiles were used.)
    `neo-apoli:direct_damaging_entity` | `neo-apoli:entity` | The owner of the projectile used for the attack (or the attacker entity if no projectiles were used.)
    `neo-apoli:broken_block` | `neo-apoli:block` | The block that was broken by a player.
    `neo-apoli:broken_side` | `neo-apoli:direction` | The side of the block broken by a player.
    `neo-apoli:mining_block` | `neo-apoli:block` | The block being mined by a player.
    `neo-apoli:selected_block` | `neo-apoli:block` | The block the player is looking at.
    `neo-apoli:applied_effect` |  | The applied status effect to an entity.
    `neo-apoli:item_in_container` | `neo-apoli:item` | The item stack from a container.
    `neo-apoli:item_in_container_slot` | `neo-apoli:slot` | The slot of the item stack from a container.
    `neo-apoli:used_item` | `neo-apoli:item` | The item stack used by an entity.
    `neo-apoli:used_item_slot` | `neo-apoli:slot` | The slot of the item stack used by an entity.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Type](#types) | | The ID of the desired parameter type.
`name` | [Identifier]({{ mc.identifier }}) | | The ID of the parameter.


### Types

- `neo-apoli:block`
- `neo-apoli:boolean`
- `neo-apoli:box`
- `neo-apoli:command_source`
- `neo-apoli:damage_source`
- `neo-apoli:direction`
- `neo-apoli:effect`
- `neo-apoli:entity`
- `neo-apoli:float`
- `neo-apoli:int`
- `neo-apoli:item`
- `neo-apoli:nbt`
- `neo-apoli:slot`
- `neo-apoli:string`
- `neo-apoli:vec3`
