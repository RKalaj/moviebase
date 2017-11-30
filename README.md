# moviebase
misy350 project

Our team project will consist of a movie database that will provide the user with information about certain movies.

The database will consist of multiple tables with some containing multiple columns.

We will have the following tables in our database:
  -movies
  -movie
  -director
  -movie-all
  -movie-add
  -director-all
  -director-add

The movie table will have the following fields:
  -ID
  -Name
  -Year
  -director.id

The director table will have the following fields:
  -director.id
  -Name
  -about
  -movies

The movie-all table will have the following fields:
  -Name
  -Year
  -director
  -id

The movie-add table will have the following fields:
  -Name
  -about
  -id

The director-all table will have the following fields:
  -Name
  -about
  -id

The director-add table will have the following fields:
  -Name
  -about
  -id



The director table will have one to many relationship with the movie table. It will a one to many because a movie can have only one director, but a director can have multiple movies.

The movie-all table will have a one to one relationship with the movie table. However, the director-all could be a one to many relationship with the movie and director tables.

The director-add table will have a one to one relationship with the director table. The movie-add table will have a one to one relationship as well with the movie table.
