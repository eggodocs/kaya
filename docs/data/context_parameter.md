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
