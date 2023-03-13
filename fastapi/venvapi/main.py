from fastapi import FastAPI
from fastapi.params import Body
from fastapi import Response
from pydantic import BaseModel
from typing import Optional
from fastapi import status
from fastapi import HTTPException
import psycopg2.extras


app = FastAPI()

class Food(BaseModel):
    name: str
    image: bytes
    price: int
    cuisine_id: int
    tried: bool = False
    rating: Optional[int] = None

global conn, cursor
def database_connection():
    global conn, cursor
    try:
        conn = psycopg2.connect(host='0.0.0.0', database='postgres', user='postgres', password='fastapi24', cursor_factory=psycopg2.extras.RealDictCursor)
        cursor = conn.cursor()
        print("[INFO main.py] Database connection is succesfull!")
    except Exception as e:
        print("[INFO main.py] Database connection is failed! ", e)

categories = {0:"breakfast", 1:"lunch", 2:"dinner"}
my_posts = [{"title":"Sunny side-up", "content":"One egg, butter, salt", "category":0, "published":True, "rating": 4, "id":1},
            {"title":"Scrumbled eggs with Croissant", "content":"One egg, butter, salt, flour, sugar, milk, yeast", "category":1, "published":True, "rating": 5, "id":2},
            {"title":"Pesto Penne", "content":"penne pasta, basit pesto, salt, black pepper, cherry tomatoes, parmesan cheese", "category":2, "published":False, "rating": 5, "id": 3}]


# def create_menu():
#     global conn, cursor
#     sql_query = 


database_connection() # start connection
create_menu() # create menu from database

def find_food_by_id(id):
    for food in my_foods:
        if post["id"] == id:
            return post

def find_index_post_by_id(id):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i
# decorator, get request to api
@app.get("/") # / means localhost
async def root(): #async is not a must here we are doing simple stuff
    return {"message": "welcome to api change"} #send to fastapi, it converts to json

# get posts api
@app.get("/posts") 
def get_posts():
    return {"data":my_posts}

# create a post api
# @app.post("/createposts")
# def create_posts(payLoad: dict = Body()):
#     print(payLoad)
#     return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}

@app.post("/posts")
def create_posts(post: Post, status_code = status.HTTP_201_CREATED):
    print(post.dict())
    dict = post.dict()
    dict["id"] = len(my_posts)+1
    my_posts.append(dict)
    return {"data": dict}

# title string, content string, category string 

# latest can be considered as id so put it above
@app.get("/posts/latest")
def get_latest_post():
    latest_post = my_posts[-1]
    return {"detail":latest_post}

@app.get("/posts/{id}")
def get_post(id: int, response: Response): # get post by id
    post = find_post_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    #    response.status_code = status.HTTP_404_NOT_FOUND
    #    return {"Error message": f"post with id: {id} was not found"}
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, response: Response):
    index = find_index_post_by_id(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found, therefore not deleted")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# at least we should give non-optional non-default variables of class
# title content category
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    print(post) 

    index = find_index_post_by_id(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found, therefore not deleted")
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}

# @app.patch("/posts/{id}")
# def update_post2(id: int, post: Post):
#     print(post)

#     index = find_index_post_by_id(id)
#     if not index:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                             detail=f"post with id: {id} was not found, therefore not deleted")
#     post_dict = post.dict()
    
#     for key, value in post_dict.keys(), post_dict.values():
#         my_posts[index][key] = value
    
#     print(my_posts[index])
#     return{"message" : "update patch"}




