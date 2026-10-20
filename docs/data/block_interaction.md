#   Block Interaction

A [string][string] that determines how an explosion interacts with its affected blocks.


{% if block_interactions %}

### Values

Value | Description
------|------------
{%- for block_interaction in block_interactions %}
`{{ block_interaction.name}}` | {{ block_interaction.description}}
{%- endfor %}
{% endif %}
