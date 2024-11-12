class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev_site.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/yourdatabase'

config = {
    "default": Config,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
