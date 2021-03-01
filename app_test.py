from flask import Flask, render_template


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")


@app.route('/1/')
def index():
    """ Главная страница """
    return render_template(
        'index1.html',
    )


@app.route('/2/')
def index2():
    """ Главная страница """
    return render_template(
        'index2.html',
    )


@app.route('/3/')
def index3():
    """ Главная страница """
    return render_template(
        'index3.html',
    )


@app.route('/4/')
def index4():
    """ Главная страница """
    return render_template(
        'index_bootstrap.html',
    )
app.run()
