#   Context Parameter

An object that determines a parameter, which indicates what kind of object is stored in a context.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Type](#types) | | The ID of the desired parameter type.
`name` | [Identifier]({{ mc.identifier }}) | | The ID of the parameter.


### Types

Most if not all parameter types have a corresponding value provider. Check the table below for the available parameter types and its corresponding value provider:

Type | Value Provider
-----|-----------------------------
`neo-apoli:block` | [Block Provider][block_provider]
`neo-apoli:boolean` | [Boolean Provider][boolean_provider]
`neo-apoli:box` | [Box Provider][box_provider]
`neo-apoli:command_source` | [Command Source Provider][command_source_provider]
`neo-apoli:damage_source` | [Damage Source Provider][damage_source_provider]
`neo-apoli:direction` | [Direction Provider][direction_provider]
`neo-apoli:effect` | [Effect Provider][effect_provider]
`neo-apoli:entity` | [Entity Provider][entity_provider]
`neo-apoli:float` | [Float Provider][float_provider]
`neo-apoli:int` | [Int Provider][int_provider]
`neo-apoli:item` | [Item Provider][item_provider]
`neo-apoli:nbt` | [NBT Provider][nbt_provider]
`neo-apoli:slot` | [Slot Provider][slot_provider]
`neo-apoli:string` | [String Provider][string_provider]
`neo-apoli:vec3` | [Vec3 Provider][vec3_provider]


### Pre-defined Parameters

In neo-apoli, there are pre-defined context parameters that are used/shared by certain types:

Parameter | Type |Description
----------|------|-----------
`neo-apoli:command/entity` | `neo-apoli:entity` | Refers to the entity that executed the command.
`neo-apoli:command/position` | `neo-apoli:vec3` | Refers to the position of the executed command.
`neo-apoli:actor_entity` | `neo-apoli:entity` | Usually refers to an entity that did an action. (e.g: the attacker)
`neo-apoli:target_entity` | `neo-apoli:entity` | Usually refers to the entity that was targeted. (e.g: the victim)
`neo-apoli:projectile_entity` | `neo-apoli:entity` | Refers to a projectile entity.
`neo-apoli:this_entity` | `neo-apoli:entity` | Usually refers to the entity holding a power.
`neo-apoli:dealt_damage_source` | `neo-apoli:damage_source` | The damage source dealt by an entity.
`neo-apoli:taken_damage_source` | `neo-apoli:damage_source` | The damage source taken by an entity.
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
