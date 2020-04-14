import os
import json
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# import data model
from models import setup_db, Movie, Actor

# import authorization file
from auth import AuthError, requires_auth


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


##ROUTES
  @app.route('/')
  def homepage():
      return 'Capstone Project!'

#Movie Routes
  @app.route('/movies', methods=['GET'])
  def get_movies():
      all_movies = Movie.query.all()
      movies = [Movie.format(movie) for movie in all_movies]
      res = jsonify({
          'success': True,
          'movies': movies
      })
      return res

  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movie')
  def post_movies(token):
      body = request.get_json()  

      new_title = body.get('title')
      new_releasedate = body.get('releasedate')
      try:
          new_movie = Movie(title=new_title, releasedate=new_releasedate)
          new_movie.insert()
          return jsonify({
              'success': True,
              'movies': Movie.format(new_movie)
          })
      except Exception:
          abort(422)

  @app.route("/movies/<movie_id>", methods=['PATCH'])
  @requires_auth("patch:movie")
  def patch_movies(token,movie_id):
      new_movie_info = json.loads(request.data.decode('utf-8'))
      movie_info = Movie.query.get(movie_id)
      if 'title' in new_movie_info:
          setattr(movie_info, 'title', new_movie_info['title'])
      if 'releasedate' in new_movie_info:
          setattr(movie_info, 'releasedate', new_movie_info['releasedate'])
      Movie.update(movie_info)
      movies = list(map(Movie.format, Movie.query.all()))
      res = jsonify({
          "success": True,
          "movies": movies
      })
      return res

  @app.route("/movies/<movie_id>", methods=['DELETE'])
  @requires_auth("delete:movie")
  def delete_movies(token, movie_id):
      movie_info = Movie.query.get(movie_id)
      Movie.delete(movie_info)
      movies = list(map(Movie.format, Movie.query.all()))
      res = jsonify({
          "success": True,
          "movies": movies
      })
      return res


#Actor Routes
  @app.route('/actors', methods=['GET'])
  def get_actors():
      all_actors = Actor.query.all()
      actors = [Actor.format(actor) for actor in all_actors]
      res = jsonify({
          'success': True,
          'actors': actors
      })
      return res

  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actor')
  def post_actors(token):
      body = request.get_json()  

      new_name = body.get('name')
      new_age = body.get('age')
      new_gender = body.get('gender')
      try:
          new_actor = Actor(name=new_name, age=new_age, gender=new_gender)
          new_actor.insert()
          return jsonify({
              'success': True,
              'actors': Actor.format(new_actor)
          })
      except Exception:
          abort(422)

  @app.route("/actors/<actor_id>", methods=['PATCH'])
  @requires_auth("patch:actor")
  def patch_actors(token,actor_id):
      new_actor_info = json.loads(request.data.decode('utf-8'))
      actor_info = Actor.query.get(actor_id)
      if 'name' in new_actor_info:
          setattr(actor_info, 'name', new_actor_info['name'])
      if 'age' in new_actor_info:
          setattr(actor_info, 'age', new_actor_info['age'])
      if 'gender' in new_actor_info:
          setattr(actor_info, 'gender', new_actor_info['gender'])
      Actor.update(actor_info)
      actors = list(map(Actor.format, Actor.query.all()))
      res = jsonify({
          "success": True,
          "actors": actors
      })
      return res

  @app.route("/actors/<actor_id>", methods=['DELETE'])
  @requires_auth("delete:actor")
  def delete_actors(token, actor_id):
      actor_info = Actor.query.get(actor_id)
      Actor.delete(actor_info)
      actors = list(map(Actor.format, Actor.query.all()))
      res = jsonify({
          "success": True,
          "actors": actors
      })
      return res

  
  ## Error Handling
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  @app.errorhandler(404)
  def notfound(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "resource not found"
                      }), 404

  @app.errorhandler(AuthError)
  def auth_error(e):
      return jsonify(e.error), e.status_code


  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)