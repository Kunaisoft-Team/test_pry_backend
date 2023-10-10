from fastapi import FastAPI
from app.v1.routes import user_routes,post_routes
import app.v1.sql_app as sql_app



sql_app.Base.metadata.create_all(bind=sql_app.engine)




app = FastAPI(title="Post test",version="0.1.0")



app.include_router(user_routes.router,prefix="/api/v1")
app.include_router(post_routes.router,prefix="/api/v1")