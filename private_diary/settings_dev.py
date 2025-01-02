from .settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3g9df@6_nu)rv4cdd1e^$iy8re7^w%vtri+q6&s#vl+bmd8y1c"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# ロギング設定
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    # ロガー設定
    "loggers": {
        # djangoのロガー
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        # diaryアプリケーションのロガー
        "diary": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
    # ハンドラの設定
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev",
        },
    },
    # フォーマッターの設定
    "formatters": {
        "dev": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(pathname)s(Line:%(lineno)d)",
                    "%(message)s",
                ]
            )
        }
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# 起動方法
# source ../bin/activate
# vscodeの実行とデバッグから起動
# ↑.vscodeのlaunch.json の起動スクリプトを実行
# superuser
# shuhasegawa m
# shuhasegawa0430@gmail.com
