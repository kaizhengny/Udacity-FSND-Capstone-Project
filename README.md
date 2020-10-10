This is a casting agency app with movies and actors data. It is hosted on Heroku with below domain:

Domain:  https://capstone-kaiz.herokuapp.com/

Dependencies:
    Run pip install -r requirements.txt to install the dependencies Set the variable FLASK_APP=app.py Run the command "flask run" to start

App Test:
    To run the test suite, run "python test_app.py"
    The "capstone-test.pgsql" could be used to set up testing databse

Roles:
    Casting Assistant: 
        Can view actors and movies
    Casting Director : 
        All permissions a Casting Assistant has, Add or delete an     actor from the database, Modify actors or movies
    Executive Director: 
        All permissions a Casting Director has, Add or delete a movie from the database

Auth0:
    This app use Auth0 for authentication and authorization services. Information for Postman testings are included in capston-kaiz.postman_collection.json file. Authentication tokens and respective permissions for each role are also listed below: 

    Casting Assistant:
        Permission: 
        get:movie, get:actor
        
        Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpUV21RNmIyWGp4R3FGMnh0RlVNQyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLWt6LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk1ZDM4N2QzMTBkODBjMGY1MzgyMmIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4Njg5NzEyNSwiZXhwIjoxNTg2OTgzNTI1LCJhenAiOiJtcjlBbUM5N05UeUMxMzc2VTVOYjBHc1VrckxRanNEVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIl19.p5IExGDmS2y5jhTgIX0yZNKl9VQ8zpuAyDbs9neH1qQhQ4SzVfdBfsIwxfcNWUEmnExDwH-SxJsU1sfRYzr7XcFaP_IWcvjjsRZInevk5o87vUYZaLQ2Yv3TdUk6HjbNiyrv7SzrQq6erV-9kQFI2PmhZWNVVpfPRu1ybR8yTflyZG8rl2aK5_RrRhn-ErTiRO-AMrjnN_DnG7lT3wZoaVrG-cFGuBeY0lSkbWOu2zq0WQQxYQHqtT1yUgXyjhaRLBHZkpg_9CXHBoJ5D5b7z3B-bDcX2xsbw-6nHuzd6vNpmIk_MGJaQpAFQKHJj3xe2C315dg2QU8__eo65BjOJw

    Casting Director
        Permission: 
        get:movie, patch:movie, get:actor, post:actor, patch:actor, delete:actor
        
        Token: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpUV21RNmIyWGp4R3FGMnh0RlVNQyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLWt6LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk1ZDNiYTRhZDdiYjBjMTA2MThiMjciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4Njg5Njc3NSwiZXhwIjoxNTg2OTgzMTc1LCJhenAiOiJtcjlBbUM5N05UeUMxMzc2VTVOYjBHc1VrckxRanNEVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.NS0acLx-HWlJAqh5TO6bWvAPMIGLDtuYCGb6gm-IHgoUh4t3kr-JdpLSwhqusqu6AG6aQb-OjjthwhAanIOq-u55NL5pmhJtpgmBXjHq6rDMrw1Jm2eKIO0NGTBTo0U1SAC3-ZuQA9_fUUJXV6JH5_8ipXGYfhxVYQpROV8_ntyRuQOhyvF3em5s7e1x0Or-s1hlA_25RyllPkJEGboGg2RP4V36fLVLbw0GFwjL2WseIhxoTqo-a2acdGGOSxm2SZIJgR9x_8vpg5ub7GxT4EPGkHFnf83lAbCNA1uDLCHpr147rda9pxQCrdfss_lZefUNj1-3w3bGBrPby4uGbQ


    Executive Director
        Permission: 
        get:movie, post:movie, patch:movie, delete:movie, get:actor, post:actor, patch:actor, delete:actor
        
        Token:
        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkpUV21RNmIyWGp4R3FGMnh0RlVNQyJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b25lLWt6LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTk1ZDNlZjI5YWIzYzBjMTA1NDA2ODIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU4Njg5Njk5NywiZXhwIjoxNTg2OTgzMzk3LCJhenAiOiJtcjlBbUM5N05UeUMxMzc2VTVOYjBHc1VrckxRanNEVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.u_1qkOQTA8K3s1eQ1OuABha-_c2vvmKb61VoEGyoRXN6bhftV5dR8ygCEomOpJmS_ecOFI7MUUDaj_RwAXpkmGyvaopzPpGyyuL5pP35PHaNiL-1sizcD-CVA8qWqcidNf3zgM4t7-205czwQgG-neKwqd6AqGLJKVZ5LysfjW9vcobxTM-nN309kUC1fz3_tX605uX9V6R4vNXv3wzkCB7YuIN1w-VlyPkgOXKR4-GW-aIyvjEzoPgMxyvom143f85-OMJebUmw4fe-s9LsY0GogKVGB5z-Y75pzp1FMoe4Hx4mc10Mndi5YWQtzFgzu3Vikknw4O-tMWCQ9CtCMg

API Routes:
    GET '/movies' -Returns a list of all movies in the database

    GET '/actors' -Returns a list of all actors in the database

    POST '/movies' -Takes a dictionary object in the request body with the following format and creates a new movie: { 'title': String, 'releasedate': String }

    POST '/actors' -Takes a dictionary object in the request body with the following format and creates a new actor: { 'name': String, 'age': Integer, 'gender': String }

    PATCH '/movies/' -Takes an id from the request URL and finds the corresponding movie to update with the provided information in the request body

    PATCH '/actors/' -Takes an id from the request URL and finds the corresponding actor to update with the provided information in the request body

    DELETE '/movies/' -Takes an id from the request URL and finds the corresponding movie to delete

    DELETE '/actors/' -Takes an id from the request URL and finds the corresponding actor to delete
