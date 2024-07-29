import sentry_sdk
from sentry_sdk.integrations.threading import ThreadingIntegration

def construct_dsn(config):
    return f"{config['protocol']}://{config['public_key']}@{config['host']}:{config['port']}/{config['project_id']}"

def init_drcode(config):
    dsn = construct_dsn(config)
    
    sentry_sdk.init(
        dsn=dsn,
        integrations=[
            ThreadingIntegration(propagate_hub=True),
        ],
        traces_sample_rate=config.get('traces_sample_rate', 1.0),
        profiles_sample_rate=config.get('profiles_sample_rate', 1.0),
    )
