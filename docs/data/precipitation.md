#   Precipitation

A [string][string] that indicates the weather of a biome at a position.


{% if precipitations %}

### Values

Value | Description
------|------------
{%- for precipitation in precipitations %}
`{{ precipitation.name}}` | {{ precipitation.description}}
{%- endfor %}
{% endif %}
