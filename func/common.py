from func.camel_case_transform import to_camel_case, to_pascal_case, to_kebab_case


def replace_path_name(path: str, new_name: str) -> str:
    return path.replace('templateCode', to_camel_case(new_name)).replace('TemplateCode', to_pascal_case(new_name))


def replace_root_path(root: str) -> str:
    return root.replace('_template_code', 'src')