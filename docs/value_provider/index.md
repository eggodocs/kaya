#   Value Provider

Value providers are data objects that operate on a given context and return an object value based on the parameters provided by the said context. These can be used for providing dynamic values for fields where a context is given.


### Format

Field | Type | Default | Description
------|------|:-------:|------------
`type` | [Kind](#kinds) | | The ID of the desired kind of value provider.
`value` | Provider | | The value to provide.


???+ info "Kind"

    A value provider has a "kind" which determines what type of object it will provide and what type of context parameter it can create. This allows for creation of value providers in fields or codecs without restriction on the type. (See: [Context Parameter Map][context_parameter_map])


    ### Kinds

    Kind and Parameter Type | Provider
    ------------------------|---------
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
