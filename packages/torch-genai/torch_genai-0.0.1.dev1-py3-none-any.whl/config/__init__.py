def get_obj_from_str(s, reload=False):
    import importlib
    module, cls = s.rsplit(".", 1)
    if reload:
        module_imp = importlib.import_module(module)
        importlib.reload(module_imp)
    return getattr(importlib.import_module(module, package=None), cls)


def instantiate_from_config(config):
    if not "target" in config:
        raise KeyError("Expected key `target` to instantiate.")
    t0 = config["target"]
    t1 = config.get("params", dict())
    t2 = get_obj_from_str(t0)
    return t2(**t1)


if __name__ == "__main__":
    o = get_obj_from_str('torch.nn.GELU')
    print(o)