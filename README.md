# imdb_daraset_RESTAPI_python
Provides REST APIs for the IMDB dataset

MySQL is used for storage purpose of the IMDB database. Other NoSQL database would be better choice in place of this considering the cases of searching using patterns.

Following is the image shows the ERD of the Database in my localhost.
---
![plot](./ERD.png)


---

# API's which can be used are:

```
http://127.0.0.1:8000/moviesAPI/rating/5/9/0
(http://127.0.0.1:8000/moviesAPI/rating/{min_rating}/{max_rating}/{offset})
```
```
http://127.0.0.1:8000/moviesAPI/director/byname/jhon
(http://127.0.0.1:8000/moviesAPI/director/byname/{pattern})
```
```
http://127.0.0.1:8000/moviesAPI/director/byID/nm005690
(http://127.0.0.1:8000/moviesAPI/director/byID/{ID})
```
```
http://127.0.0.1:8000/moviesAPI/director/byID/nm005690/movies
(http://127.0.0.1:8000/moviesAPI/director/byID/{ID}/movies)
```
```
http://127.0.0.1:8000/moviesAPI/movie-by-pattern/"iron man"
(http://127.0.0.1:8000/moviesAPI/movie-by-pattern/{pattern})
```
