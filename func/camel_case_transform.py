# 转换为camelCase
def to_camel_case(snake_str: str) -> str:
    components = snake_str.lower().split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


# 转换为CamelCase
def to_pascal_case(snake_str: str) -> str:
    components = snake_str.lower().split('_')
    return ''.join(x.title() for x in components)