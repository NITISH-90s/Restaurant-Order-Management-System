class Config:
# ======================================================
# DATABASE CONFIGURATION
# ======================================================

 SQLALCHEMY_DATABASE_URI = "sqlite:///restaurant.db"

 SQLALCHEMY_TRACK_MODIFICATIONS = False


# ======================================================
# SECRET KEYS
# ======================================================

 SECRET_KEY = "supersecretkey"

 JWT_SECRET_KEY = "jwtsecretkey"


# ======================================================
# MAIL CONFIGURATION
# ======================================================

 MAIL_SERVER = "smtp.gmail.com"

 MAIL_PORT = 587

 MAIL_USE_TLS = True

 MAIL_USE_SSL = False

 MAIL_USERNAME = "your_email@gmail.com"

 MAIL_PASSWORD = "your_app_password"


# ======================================================
# UPLOAD CONFIGURATION
# ======================================================

 UPLOAD_FOLDER = "static/images"

 MAX_CONTENT_LENGTH = 16 * 1024 * 1024


# ======================================================
# SOCKETIO CONFIGURATION
# ======================================================

 SOCKETIO_ASYNC_MODE = "eventlet"


# ======================================================
# SESSION CONFIGURATION
# ======================================================

 SESSION_PERMANENT = False

 SESSION_TYPE = "filesystem"


# ======================================================
# DEBUG MODE
# ======================================================

 DEBUG = True