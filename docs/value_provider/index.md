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
    `kaya:block` | [Block Provider][block_provider]
    `kaya:boolean` | [Boolean Provider][boolean_provider]
    `kaya:box` | [Box Provider][box_provider]
    `kaya:command_source` | [Command Source Provider][command_source_provider]
    `kaya:damage_source` | [Damage Source Provider][damage_source_provider]
    `kaya:direction` | [Direction Provider][direction_provider]
    `kaya:effect` | [Effect Provider][effect_provider]
    `kaya:entity` | [Entity Provider][entity_provider]
    `kaya:float` | [Float Provider][float_provider]
    `kaya:int` | [Int Provider][int_provider]
    `kaya:item` | [Item Provider][item_provider]
    `kaya:nbt` | [NBT Provider][nbt_provider]
    `kaya:slot` | [Slot Provider][slot_provider]
    `kaya:string` | [String Provider][string_provider]
    `kaya:vec3` | [Vec3 Provider][vec3_provider]
