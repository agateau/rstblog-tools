import os


CONFIG_FILE_PATH = os.environ.get('RSTBLOG_TOOLS_CONFIG',
                                  os.path.expanduser('~/.config/rstblog-tools.conf'))

def load():
    print('Loading config from {}'.format(CONFIG_FILE_PATH))
    cfg = {}
    with open(CONFIG_FILE_PATH) as fp:
        dct = {}
        exec(fp.read(), dct, cfg)
    return cfg
