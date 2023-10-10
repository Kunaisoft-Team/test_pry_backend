from fastapi import APIRouter,Depends,Body,status
from cachetools.func import ttl_cache
import datetime
from app.v1.controllers.auth_controller import get_current_user
from app.v1.schemas import Post
from app.v1.sql_app import get_db
import app.v1.sql_app as sql_app

router = APIRouter(tags=["Posts"])

@router.post("/posts",status_code=status.HTTP_201_CREATED,tags=["Posts"])
async def create_post(
post:Post = Body(...),
db = Depends(get_db),
current_user = Depends(get_current_user)
):

    return sql_app.create_user_post(db=db,item=post,user_id=current_user.id)


@ttl_cache(maxsize=100,ttl=60*60,timer=lambda : datetime.timedelta(minutes=5))
@router.get("/posts",status_code=status.HTTP_200_OK,tags=["Posts"])
async def get_posts(db = Depends(get_db),current_user = Depends(get_current_user)):
    return sql_app.get_posts(db=db,skip=0,limit=100,user=current_user)



@router.get("/posts/{id}",status_code=status.HTTP_200_OK,tags=["Posts"])
async def get_post(id:int,db = Depends(get_db),current_user = Depends(get_current_user)):
    return sql_app.get_post(db=db,id=id,user=current_user)




@router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT,tags=["Posts"])
async def delete_post(id:int,db = Depends(get_db),current_user = Depends(get_current_user)):
    sql_app.delete_post(db=db,id=id,user=current_user)