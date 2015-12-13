import os


CONFIG_FILE_PATH = os.environ.get('RSTBLOG_TOOLS_CONFIG',
                                  os.path.expanduser('~/.config/rstblog-tools.conf'))


def _expand(value):
    return os.path.expandvars(os.path.expanduser(value))


def load():
    print('Loading config from {}'.format(CONFIG_FILE_PATH))
    cfg = {}
    with open(CONFIG_FILE_PATH) as fp:
        dct = {}
        exec(fp.read(), dct, cfg)
    for key, value in cfg.items():
        cfg[key] = _expand(value)
    return cfg
