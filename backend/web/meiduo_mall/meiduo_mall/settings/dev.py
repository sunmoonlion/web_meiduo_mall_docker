import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import datetime
from pathlib import Path

import meiduo_mall.utils.fastdfs.fdfs_storage

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# print(BASE_DIR)

# 查看导包路径
# print(sys.path)
# 追加导包路径指向apps包
# sys.path.insert(0, '/home/zym/Documents/projects/meiduo_project/meiduo_mall/meiduo_mall/apps')
sys.path.insert(0, os.path.join(BASE_DIR, 'meiduo_mall/apps'))
# print(sys.path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pywy*dhbub(60m4$jdt*v*2&4x&tum(sphoti&yyet@v_pn=bh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # 'meiduo_mall.apps.users', # 用户模块
    'users',  # 用户模块
    'contents',  # 首页广告模块
    'verifications',  # 验证码模块
    'oauth',  # 第三方登录
    'areas',  # 省市区三级联动
    'goods',  # 商品模块
    'carts',  # 购物车
    'orders',  # 订
    'payment',  # 支付o
    'meiduo_admin',
    'corsheaders',  # 跨域模块
    'rest_framework',
    'haystack',
    'django_crontab',  # 定时任务
    'django_filters',  #过滤

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduo_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',  # 配置Jinja2模板引擎
        'DIRS': [BASE_DIR / 'meiduo_mall/templates'],  # 配置模板文件加载路径
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 补充Jinja2模板引擎环境
            'environment': 'meiduo_mall.utils.jinja2_env.jinja2_environment',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },

]

WSGI_APPLICATION = 'meiduo_mall.wsgi.application'

# Databasepip install elasticsearch==2.4.1
# https://docs.djangoproject.com/en/1.11/ref/settings/#databasespip install elasticsearch==2.4.1

DATABASES = {
    'default': {#写（主机）
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': 'db_master',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'zym',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'meiduo_mall'  # 数据库名字
    },
    'slave': {#读（从机）
        'ENGINE': 'django.db.backends.mysql',  # 数据库引擎
        'HOST': 'db_slave',  # 数据库主机
        'PORT': 8306,  # 数据库端口
        'USER': 'zym',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'meiduo_mall' # 数据库名字
    }
}

# 配置Redis数据库
CACHES = {
    "default": {  # 默认
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {  # session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify_code": {  # 验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "history": { # 用户商品浏览记录
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "carts": { # 购物车
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/



# 配置静态文件加载路径
STATICFILES_DIRS = [BASE_DIR / 'meiduo_mall/static']

# 配置工程日志
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/meiduo.log',  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# 指定自定义的用户模型类：值的语法 ==> '子应用.用户模型类'
AUTH_USER_MODEL = 'users.User'

# 指定自定义用户认证后端
# AUTHENTICATION_BACKENDS = ['meiduo_mall.utils.authenticate.MeiduoModelBackend']
AUTHENTICATION_BACKENDS = ['users.utils.MeiduoModelBackend']
# 判断用户是否登录后，指定未登录用户重定向的地址
LOGIN_URL = '/login/'

# QQ登录的配置参数
QQ_CLIENT_ID = '101518219'
QQ_CLIENT_SECRET = '418d84ebdc7241efb79536886ae95224'
QQ_REDIRECT_URI = 'http://www.meiduo.site:8000/oauth_callback'

# 邮件参数
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 导入邮件模块
EMAIL_HOST = 'smtp.163.com'  # 发邮件主机
EMAIL_PORT = 25  # 发邮件端口
EMAIL_HOST_USER = '13701819268@163.com'  # 授权的邮箱
EMAIL_HOST_PASSWORD = 'DRAAKALDSJJNXNML'  # 邮箱授权时获得的密码，非注册登录密码
EMAIL_FROM = '美多商城<13701819268@163.com>'  # 发件人抬头

# 邮箱验证链接
EMAIL_VERIFY_URL = 'http://www.meiduo.site:8000/emails/verification/'

# 指定自定义的Django文件存储类
DEFAULT_FILE_STORAGE = 'meiduo_mall.utils.fastdfs.fdfs_storage.FastDFSStorage'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'meiduo_mall/utils/fastdfs/client.conf')
# FastDFS相关参数
FDFS_BASE_URL = 'http://192.168.83.129:8888/'
# FDFS_BASE_URL = 'http://image.meiduo.site:8888/'

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://elasticsearch:9200/',  # Elasticsearch服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo_mall',  # Elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# haystack分页时每页记录条数
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 5

# 支付宝
ALIPAY_APPID = '2016082100308405'
ALIPAY_DEBUG = True
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'
ALIPAY_RETURN_URL = 'http://www.meiduo.site:8000/payment/status/'

# 定时器配置
CRONJOBS = [
    # 每1分钟生成一次首页静态文件
    ('*/1 * * * *', 'contents.crons.generate_static_index_html', '>> ' + os.path.join(os.path.dirname(BASE_DIR), 'logs/crontab.log'))
]

# 指定中文编码格式
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# MySQL读写分离路由
DATABASE_ROUTERS = ['meiduo_mall.utils.db_router.MasterSlaveDBRouter']

# 设置STATIC ROOT 和 STATIC URL
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = "/static/"

# 设置MEDIA ROOT 和 MEDIA URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# CORS_ORIGIN_WHITELIST = (
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:8080',
# )
# CORS_ORIGIN_ALLOW_ALL为True, 指定所有域名(ip)都可以访问后端接口, 默认为False
CORS_ORIGIN_ALLOW_ALL = True
#
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

REST_FRAMEWORK = {

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],


    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
SIMPLE_JWT = {
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'AUTH_HEADER_TYPES': ("Bearer","JWT"),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',
                           'rest_framework_simplejwt.tokens.SlidingToken'),}




# JWT配置
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
#     'JWT_RESPONSE_PAYLOAD_HANDLER': 'meiduo_admin.utils.jwt_response.jwt_response_payload_handler',
# }
