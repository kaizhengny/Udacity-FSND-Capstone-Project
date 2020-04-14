import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Movie, Actor, db


class CastingTestCase(unittest.TestCase):
    """This class represents the casting test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgres://{}/{}".format('localhost:5433', self.database_name)
        setup_db(self.app, self.database_path)

        self.casting_assistant_auth = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpUV21RNmIyWGp4R3FGMnh0RlVNQyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLWt6LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk1ZDM4N2QzMTBkODBjMGY1MzgyMmIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4Njg5NzEyNSwiZXhwIjoxNTg2OTgzNTI1LCJhenAiOiJtcjlBbUM5N05UeUMxMzc2VTVOYjBHc1VrckxRanNEVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.p5IExGDmS2y5jhTgIX0yZNKl9VQ8zpuAyDbs9neH1qQhQ4SzVfdBfsIwxfcNWUEmnExDwH-SxJsU1sfRYzr7XcFaP_IWcvjjsRZInevk5o87vUYZaLQ2Yv3TdUk6HjbNiyrv7SzrQq6erV-9kQFI2PmhZWNVVpfPRu1ybR8yTflyZG8rl2aK5_RrRhn-ErTiRO-AMrjnN_DnG7lT3wZoaVrG-cFGuBeY0lSkbWOu2zq0WQQxYQHqtT1yUgXyjhaRLBHZkpg_9CXHBoJ5D5b7z3B-bDcX2xsbw-6nHuzd6vNpmIk_MGJaQpAFQKHJj3xe2C315dg2QU8__eo65BjOJw'
        }

        self.casting_director_auth = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpUV21RNmIyWGp4R3FGMnh0RlVNQyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLWt6LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk1ZDNiYTRhZDdiYjBjMTA2MThiMjciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4Njg5Njc3NSwiZXhwIjoxNTg2OTgzMTc1LCJhenAiOiJtcjlBbUM5N05UeUMxMzc2VTVOYjBHc1VrckxRanNEVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.NS0acLx-HWlJAqh5TO6bWvAPMIGLDtuYCGb6gm-IHgoUh4t3kr-JdpLSwhqusqu6AG6aQb-OjjthwhAanIOq-u55NL5pmhJtpgmBXjHq6rDMrw1Jm2eKIO0NGTBTo0U1SAC3-ZuQA9_fUUJXV6JH5_8ipXGYfhxVYQpROV8_ntyRuQOhyvF3em5s7e1x0Or-s1hlA_25RyllPkJEGboGg2RP4V36fLVLbw0GFwjL2WseIhxoTqo-a2acdGGOSxm2SZIJgR9x_8vpg5ub7GxT4EPGkHFnf83lAbCNA1uDLCHpr147rda9pxQCrdfss_lZefUNj1-3w3bGBrPby4uGbQ'
        }

        self.executive_director_auth = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpUV21RNmIyWGp4R3FGMnh0RlVNQyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLWt6LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk1ZDNlZjI5YWIzYzBjMTA1NDA2ODIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4Njg5Njk5NywiZXhwIjoxNTg2OTgzMzk3LCJhenAiOiJtcjlBbUM5N05UeUMxMzc2VTVOYjBHc1VrckxRanNEVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.u_1qkOQTA8K3s1eQ1OuABha-_c2vvmKb61VoEGyoRXN6bhftV5dR8ygCEomOpJmS_ecOFI7MUUDaj_RwAXpkmGyvaopzPpGyyuL5pP35PHaNiL-1sizcD-CVA8qWqcidNf3zgM4t7-205czwQgG-neKwqd6AqGLJKVZ5LysfjW9vcobxTM-nN309kUC1fz3_tX605uX9V6R4vNXv3wzkCB7YuIN1w-VlyPkgOXKR4-GW-aIyvjEzoPgMxyvom143f85-OMJebUmw4fe-s9LsY0GogKVGB5z-Y75pzp1FMoe4Hx4mc10Mndi5YWQtzFgzu3Vikknw4O-tMWCQ9CtCMg'
        }

        self.starting_movie = {
            'title': 'test movie 1',
            'releasedate': 'June 27, 2008'
        }

        self.new_movie = {
            'title': 'test movie 2',
            'releasedate': 'December 01, 2019'
        }

        self.patch_movie = {
            'title': 'Up'
        }

        self.starting_actor = {
            'name': 'Johnny Walker',
            'age': '25',
            'gender': 'male'
        }

        self.new_actor = {
            'name': 'James Bond',
            'age': '36',
            'gender': 'male'
        }

        self.new_actor_2 = {
            'name': 'Robert Donny',
            'age': '40',
            'gender': 'male'
        }

        self.patch_actor = {
            'age': '55'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = db
            self.db.init_app(self.app)
    
            # self.db.drop_all()
            self.db.create_all()

        #Populating test data for delete and patch test. Probably not best practice but will have to do while I learn more about mocking data.
        self.client().post('/movies', json=self.starting_movie, headers=self.executive_director_auth)
        self.client().post('/actors', json=self.starting_actor, headers=self.executive_director_auth)  
        #Different combinations of permissions for testing      
        self.permissions = [self.casting_assistant_auth, self.casting_director_auth, self.executive_director_auth]
        self.limited_permissions = [self.casting_assistant_auth, self.casting_director_auth]
        self.elevated_permissions = [self.casting_director_auth, self.executive_director_auth]

    def tearDown(self):
        """Executed after reach test"""
        self.db.drop_all()
        pass


    def test_get_movies(self):
        for permission in self.permissions:
            with self.subTest():
                res = self.client().get('/movies', headers=permission)
                data = json.loads(res.data)

                self.assertEqual(res.status_code, 200)
                self.assertIsNotNone(data['movies'])

#     def test_post_movie(self):
#         for permission in self.permissions:
#             with self.subTest():
#                 res = self.client().post('/movies', json=self.new_movie, headers=permission)
#                 #if blocks to check different permissions
#                 if permission == self.casting_director_auth or permission == self.casting_assistant_auth:
#                     self.assertEqual(res.status_code, 401)
#                 else:
#                     self.assertEqual(res.status_code, 201)

#     def test_patch_movie(self):
#         for permission in self.permissions:
#             with self.subTest():
#                 res = self.client().patch('/movies/1', json=self.patch_movie, headers=permission)
#                 #if blocks to check different permissions
#                 if permission == self.casting_assistant_auth:
#                     self.assertEqual(res.status_code, 401)
#                 else:
#                     self.assertEqual(res.status_code, 200)

#     def test_delete_movie_with_perm(self):

#         res = self.client().delete('/movies/1', headers=self.executive_producer_auth)
#         data = json.loads(res.data)

#         self.assertEqual(res.status_code, 200)
    
#     def test_delete_movie_no_perm(self):
#         for permission in self.limited_permissions:
#             with self.subTest():
#                 res = self.client().delete('/movies/1', headers=permission)
                
#                 self.assertEqual(res.status_code, 401)

#     def test_get_actors(self):
#         for permission in self.permissions:
#             with self.subTest():
#                 res = self.client().get('/actors', headers=permission)
#                 data = json.loads(res.data)

#                 self.assertEqual(res.status_code, 200)
#                 self.assertIsNotNone(data['actors'])
# #need to break into different tests
#     def test_post_actor_casting_assistant(self):
#         res = self.client().post('/actors', json=self.new_actor, headers=self.casting_assistant_auth)
        
#         self.assertEqual(res.status_code, 401)

#     def test_post_actor_casting_director(self):
#         res = self.client().post('/actors', json=self.new_actor, headers=self.casting_director_auth)
        
#         self.assertEqual(res.status_code, 201)

#     def test_post_actor_executive_producer(self):
#         res = self.client().post('/actors', json=self.new_actor, headers=self.executive_producer_auth)
        
#         self.assertEqual(res.status_code, 201)

#     def test_patch_actor(self):
#         for permission in self.permissions:
#             with self.subTest():
#                 res = self.client().patch('/actors/1', json=self.patch_actor, headers=permission)
#                 #if blocks to check different permissions
#                 if permission == self.casting_assistant_auth:
#                     self.assertEqual(res.status_code, 401)
#                 else:
#                     self.assertEqual(res.status_code, 200)

#     def test_delete_actor_casting_assistant(self):
#         res = self.client().delete('/actors/1', headers=self.casting_assistant_auth)

#         self.assertEqual(res.status_code, 401)

#     def test_delete_actor_casting_director(self):
#         res = self.client().delete('/actors/1', headers=self.casting_director_auth)

#         self.assertEqual(res.status_code, 200)
    
#     def test_delete_actor_executive_producer(self):
#         res = self.client().delete('/actors/1', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 200)

#     def test_delete_movie_404(self):
#         res = self.client().delete('/movies/1000', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 404)

#     def test_delete_actor_404(self):
#         res = self.client().delete('/actors/1000', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 404)

#     def test_get_actors_405(self):
#         res = self.client().delete('/actors', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 405)

#     def test_get_movies_405(self):
#         res = self.client().delete('/movies', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 405)

#     def test_patch_movies_404(self):
#         res = self.client().patch('/movies/1000', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 404)

#     def test_patch_actors_404(self):
#         res = self.client().patch('/actors/1000', headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 404)

#     def test_post_actors_422(self):
#         res = self.client().post('/actors', json={}, headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 422)

#     def test_post_movies_422(self):
#         res = self.client().post('/movies', json={}, headers=self.executive_producer_auth)

#         self.assertEqual(res.status_code, 422)

if __name__ == "__main__":
    unittest.main()