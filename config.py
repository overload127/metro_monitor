from pathlib   import Path
import logging     as logging


class Config(object):
    # Определяет, включен ли режим отладки
    # В случае если включен, flask будет показывать
    # подробную отладочную информацию. Если выключен -
    # - 500 ошибку без какой либо дополнительной информации.
    DEBUG                     = False
    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED              = True
    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY                = 'DSFDSFSDFSDFADFASFSDFFSDBGSDGRT43432V42GRV4G'
    # Максимально допустимый размер файлов (20 mb)
    # На локальном сервере работает не правильно. Только для wsgi. 413
    MAX_CONTENT_LENGTH        = 20 * 1024 * 1024
    # Корневая папка
    BASE_DIR                  = Path(__file__).resolve().parent
    # Папка для логирования
    LOG_DIR                   = BASE_DIR.joinpath('logs')
    # Логирование
    LOG_LEVEL                 = logging.INFO
    LOG_FORMAT                = "%(asctime)s %(levelname)-7s %(name)-25s %(funcName)-25s %(message)s"

class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL                 = logging.INFO

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # Время жизни статических файлов
    SEND_FILE_MAX_AGE_DEFAULT = 1
    # Папка с файлами для доступа пользователей
    PUBLIC_UPLOAD_FOLDER      = Config.BASE_DIR.joinpath('debug_public_upload')
    LOG_LEVEL                 = logging.DEBUG
