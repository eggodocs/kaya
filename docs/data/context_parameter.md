#   Context Parameter

An object that determines a parameter, which indicates what kind of object is stored in a context.


??? tip "Pre-defined parameters"

    In kaya, there are pre-defined context parameters that are used/shared by certain types:

    Parameter | Type |Description
    ----------|------|-----------
    `kaya:command/entity` | `kaya:entity` | Refers to the entity that executed the command.
    `kaya:command/position` | `kaya:vec3` | Refers to the position of the executed command.
    `kaya:actor_entity` | `kaya:entity` | Usually refers to an entity that did an action. (e.g: the attacker)
    `kaya:target_entity` | `kaya:entity` | Usually refers to the entity that was targeted. (e.g: the victim)
    `kaya:projectile_entity` | `kaya:entity` | Refers to a projectile entity.
    `kaya:this_entity` | `kaya:entity` | Usually refers to the entity holding a power.
    `kaya:dealt_damage/source` | `kaya:damage_source` | The damage source dealt by an entity.
    `kaya:taken_damage/source` | `kaya:damage_source` | The damage source taken by an entity.
    `kaya:dealt_damage/amount` | `kaya:float` | The amount of damage dealt to an entity.
    `kaya:taken_damage/amount` | `kaya:float` | The amount of damage taken by an entity.
    `kaya:damaging_entity` | `kaya:entity` | The projectile used for the attack (or the attacker entity if no projectiles were used.)
    `kaya:direct_damaging_entity` | `kaya:entity` | The owner of the projectile used for the attack (or the attacker entity if no projectiles were used.)
    `kaya:broken_block` | `kaya:block` | The block that was broken by a player.
    `kaya:broken_side` | `kaya:direction` | The side of the block broken by a player.
    `kaya:mining_block` | `kaya:block` | The block being mined by a player.
    `kaya:selected_block` | `kaya:block` | The block the player is looking at.
    `kaya:applied_effect` |  | The applied status effect to an entity.
    `kaya:item_in_container` | `kaya:item` | The item stack from a container.
    `kaya:item_in_container_slot` | `kaya:slot` | The slot of the item stack from a container.
    `kaya:used_item` | `kaya:item` | The item stack used by an entity.
    `kaya:used_item_slot` | `kaya:slot` | The slot of the item stack used by an entity.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Type](#types) | | The ID of the desired parameter type.
`name` | [Identifier]({{ mc.identifier }}) | | The ID of the parameter.


### Types

- `kaya:block`
- `kaya:boolean`
- `kaya:box`
- `kaya:command_source`
- `kaya:damage_source`
- `kaya:direction`
- `kaya:effect`
- `kaya:entity`
- `kaya:float`
- `kaya:int`
- `kaya:item`
- `kaya:nbt`
- `kaya:slot`
- `kaya:string`
- `kaya:vec3`
