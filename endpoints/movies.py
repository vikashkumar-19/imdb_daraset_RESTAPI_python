from fastapi import APIRouter
import json
# from models.request import ProductRequest, ProductUpdateRequest
from models.response import Response
# from models.models import Titles, Title_ratings, Title_genres, Alias_types, Episode_belongs_to, Directors, Principals, Writers, Aliases, ALias_attributes, Name_worked_as, Had_role, Known_for, Names_

from db.database import Database
from sqlalchemy import text
import mysql.connector as mc

mydb = mc.connect(
  host="localhost",
  user="root",
  password="root",
  database="imdb"
)

batch_limit = 250

# APIRouter creates path operations for product module
router = APIRouter(
    prefix="/moviesAPI",
    tags=["movies"],
    responses={404: {"description": "Not found"}},
)

database = Database()
engine = database.get_db_connection()

@router.get("/")
async def read_user():
    # session = database.get_db_session(engine)
    data = None
    response_message = "Fetching successfully"
    try:
        # sql = "select * from names_ limit 10"
        # data = session.execute(text(sql),{})
        # Retrieve movies from database
        cursor = mydb.cursor()
        cursor.execute("SELECT N.name_id, N.name_, COUNT(*) AS number_of_films \
                        FROM Names_ AS N, Had_role AS H, Titles AS T \
                        WHERE H.role_ LIKE 'James Bond' \
                        AND T.title_type LIKE 'movie' \
                        AND T.title_id = H.title_id \
                        AND N.name_id = H.name_id \
                        GROUP BY N.name_id;")
        movies = cursor.fetchall()

        # Convert movies to JSON and return
        movies_json = json.dumps(movies)
        data = movies_json
    except Exception as ex:
        print("Error : ", ex)
        response_message="Request Failed"
    error = False
    return Response(data, 200, response_message, error)



@router.get("/rating/{min_rating}/{max_rating}/{offset}")
async def movies_by_rating(min_rating:float, max_rating: float, offset:int):
    data = None
    response_message = "Fetching successfully"
    try:
        cursor = mydb.cursor()
        sql_query = "SELECT T.title_id, TR.average_rating, T.start_year, T.title_type \
                        FROM Titles AS T, title_ratings as TR \
                        WHERE TR.average_rating >= %s \
                        AND TR.average_rating <= %s \
                        AND T.title_id = TR.title_id "
        # if(order):
        #     sql_query = sql_query[:-1]+ " ORDER BY TR.average_rating ASC"
        # if(order != False):
        #     sql_query = sql_query[:-1]+ " ORDER BY TR.average_rating DESC"
        sql_query = sql_query + " LIMIT %s offset %s;"
        cursor.execute( sql_query,(min_rating, max_rating, batch_limit, offset))
        movies = cursor.fetchall()

        # Convert movies to JSON and return
        movies_json = json.dumps(movies)
        data = movies_json
    except Exception as er:
        print("Error : ", er)
        response_message="Request Failed"
    error = False
    return Response(data,200,response_message, error)

@router.get("/rating/{min_rating}")
async def movies_by_rating_min(min_rating:float):
    return movies_by_rating(min_rating=min_rating, max_rating=10)


# Director

@router.get("/director/byname/{pattern}")
async def director_by_name(pattern:str):
    data =  None
    response_message = "Fetching Successfully"
    temp = pattern.split()
    final_pattern ="" 
    for x in temp:
        final_pattern=final_pattern+"%"+x+"%"
    if(final_pattern==""):
        final_pattern="%%"
    try:
        cursor = mydb.cursor()
        sql_query = "SELECT NW.name_id, N.name_ , NW.profession \
                    FROM names_ as N, name_worked_as as NW \
                    where N.name_id = NW.name_id \
                    AND NW.profession LIKE %s \
                    AND N.name_ LIKE %s;"
        print(sql_query, final_pattern)
        cursor.execute( sql_query,(str("%director%"),final_pattern))
        res = cursor.fetchall()

        # Convert movies to JSON and return
        res = json.dumps(res)
        data = res
        
    except Exception as ex:
        print("Error : ", ex)
        response_message="Request Failed"
    error = False
    return Response(data,200,response_message, error)


@router.get("/director/byID/{ID}")
async def director_by_ID(ID:str):
    data =  None
    response_message = "Fetching Successfully"
    
    try:
        cursor = mydb.cursor()
        sql_query = "SELECT * \
                    FROM names_ as N \
                    where N.name_id = %s ;"
        cursor.execute( sql_query,[ID])
        res = cursor.fetchall()

        # Convert movies to JSON and return
        res = json.dumps(res)
        data = res
        
    except Exception as ex:
        print("Error : ", ex)
        response_message="Request Failed"
    error = False
    return Response(data,200,response_message, error)

@router.get("/director/byID/{ID}/movies")
async def director_by_ID_movies(ID:str):
    data =  None
    response_message = "Fetching Successfully"
    ID= "%"+ID+"%"
    try:
        cursor = mydb.cursor()
        sql_query = "SELECT * \
            FROM directors as D \
            JOIN titles as T ON D.title_id = T.title_id \
            JOIN title_ratings as TR on  T.title_id = TR.title_id \
            where D.name_id LIKE %s;"
        cursor.execute( sql_query,[ID])
        res = cursor.fetchall()

        # Convert movies to JSON and return
        # res = json.dumps(res)
        data = res
        
    except Exception as ex:
        print("Error : ", ex)
        response_message="Request Failed"
    error = False
    return Response(data,200,response_message, error)


@router.get("/movie-by-pattern/{pattern}")
async def movie_by_pattern(pattern:str):
    data =  None
    response_message = "Fetching Successfully"
    if(len(pattern)>=1 and pattern[0]=='"'):
        pattern = pattern[1:]
    if(len(pattern)>=1 and pattern[-1]=='"'):
        pattern = pattern[:-2]
    
    temp = pattern.split()
    final_pattern =""

    for x in temp:
        final_pattern=final_pattern+"%"+x+"%"
    if(final_pattern==""):
        final_pattern="%%"
    
    try:
        cursor = mydb.cursor()
        sql_query = "SELECT * \
                    FROM titles as T \
                    where T.primary_title LIKE %s \
                    AND T.original_title LIKE %s ;"
        print(final_pattern)
        cursor.execute( sql_query,[final_pattern,final_pattern])
        res = cursor.fetchall()

        # Convert movies to JSON and return
        print("-- ", type(res))
        # res = json.dumps(res)
        data = res
        
    except Exception as ex:
        print("Error : ", ex)
        response_message="Request Failed"
    error = False
    return Response(data,200,response_message, error)

