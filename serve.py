from app import create_app, config


if __name__ == '__main__':
    app = create_app(config.dev_config)
