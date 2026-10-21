#   Ingredient

A [string][string] that defines an ingredient to be used for recipes. If prefixed with `#`, it will define an item tag, otherwise, it will define an item.


??? note "Fabric-specific feature"

    Fabric provides a custom ingredient API that can check for further data of an item, such as its item components or other types for logic handling. To define a custom ingredient, it must be an object *(`{...}`)* and follows the format below:


    ### Format

    Field | Type | Default | Description
    ------|------|---------|------------
    `fabric:type` | [Identifier]({{ mc.identifier }}) | | The ID of the desired custom ingredient type.


    ???+ tip

        [See here](https://github.com/FabricMC/fabric-api/blob/1.21.5/fabric-recipe-api-v1/src/main/java/net/fabricmc/fabric/api/recipe/v1/ingredient/DefaultCustomIngredients.java) for a list of custom ingredient types provided by Fabric and examples.
