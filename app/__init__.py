from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")


@app.route("/1/")
def index1():
    """ Главная страница """
    return render_template(
        "index1.html",
    )


@app.route("/2/")
def index2():
    """ Главная страница """
    return render_template(
        "index2.html",
    )


@app.route("/3/")
def index3():
    """ Главная страница """
    return render_template(
        "index3.html",
    )


@app.route("/4/")
def index4():
    """ Главная страница """
    return render_template(
        "index_bootstrap.html",
    )

################################################################
navbar = [
    {"url": "index", "text": "Главная"},
    {"url": "block_view", "text": "Блоки"},
    {"url": "table_view", "text": "Таблица"},
    {"url": "map_view", "text": "Карта"},
]


@app.route("/")
def index():
    """ Главная страница """
    content = dict()
    content["navbar"] = navbar
    content["current_page"] = "index"

    return render_template(
        "pages/index.html",
        content=content,
    )


@app.route("/block/")
def block_view():
    """ Вывод ввиде блоков """
    content = dict()
    content["navbar"] = navbar
    content["current_page"] = "block_view"

    return render_template(
        "pages/block.html",
        content=content,
    )


@app.route("/table/")
def table_view():
    """ Вывод ввиде таблици """
    content = dict()
    content["navbar"] = navbar
    content["current_page"] = "table_view"
    
    return render_template(
        "pages/table.html",
        content=content,
    )


@app.route("/map/")
def map_view():
    """ Вывод ввиде карты """
    content = dict()
    content["navbar"] = navbar
    content["current_page"] = "map_view"
    
    return render_template(
        "pages/map.html",
        content=content,
    )
