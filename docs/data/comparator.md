#   Comparator

A [string][string] that indicates how a two comparable objects should be compared.


### Values

Value | Description
------|------------
{% set separator = joiner("\n") %}{% for comparator in comparators %}{{ separator() }}`{{ comparator.name }}` | {{ comparator.description }}{% endfor %}
