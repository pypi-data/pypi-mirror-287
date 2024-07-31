from flask import Flask


def init_user(app: Flask):
    from webcoreframe.application import engine
    from .users.models import init_db
    init_db(engine)

    from .users.urls import init_app
    init_app(app)


def init_sys_monitor(app: Flask):
    from .sys_monitor.urls import init_app
    init_app(app)


def init_admin(app: Flask):
    from webcoreframe.application import engine
    from .admin.models import init_db
    init_db(engine)
    
    from .admin.urls import init_app
    init_app(app)


def init_contrib(app: Flask):
    init_user(app)
    init_sys_monitor(app)
    init_admin(app)
