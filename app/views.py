from flask import request, render_template, url_for, redirect
from app import app
from app.use_case import *


@app.route('/', methods=['GET'])
def index():
    m_data = use_case_index_movie() 
    h_data = use_case_index_hall()
    return render_template('index.html', movie_data = m_data, hall_data = h_data)




@app.route('/add_hall', methods=['POST'])
def api_add_hall():
    name = request.form.get('name')
    row = int(request.form.get('row'))
    column = int(request.form.get('column'))
    use_case_add_hall(name, row, column)
    return redirect(url_for('index'))


@app.route('/del_hall', methods=['POST'])
def api_del_hall():
    hall = request.get_json().get('name')
    use_case_del_hall(hall)
    return redirect(url_for('index'))


@app.route('/hall/<id>', methods=['GET'])
def api_hall(id):
    data = use_case_hall_session_list(id)
    return render_template('hall.html', session_list = data)




@app.route('/add_movie', methods=['POST'])
def api_add_movie():
    name = request.form.get('name')
    use_case_add_movie(name)
    return redirect(url_for('index'))


@app.route('/del_movie', methods=['POST'])
def api_del_movie():
    movie = request.get_json().get('name')
    use_case_del_movie(movie)
    return redirect(url_for('index'))



@app.route('/movie/<id>', methods=['GET'])
def api_movie(id):
    data = use_case_movie_session_list(id)
    return render_template('movie.html', movie_list = data)




@app.route('/session/<id>', methods=['GET'])
def api_session(id):
    data = use_case_get_session(int(id))
    return render_template('session.html', session_id = id, session_data = data)


@app.route('/update_session', methods=['POST'])
def api_update_session():
    session_id = int(request.form.get('session_id'))
    row = int(request.form.get('row'))
    column = int(request.form.get('column'))
    use_case_update_session(session_id, row, column)
    return redirect(url_for('api_session', id = session_id))


@app.route('/gen_session', methods=['POST'])
def api_gen_session():
    use_case_gen_session()
    return redirect(url_for('index'))
