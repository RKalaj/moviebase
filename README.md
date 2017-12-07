# Misy350 project
# Moviebase:


* Our team project will consist of a movie database that will provide the user with information about certain movies.

* The database will consist of multiple tables with some containing multiple columns.

# Tables:
  * movies
  * movie
  * director
  * movie-all
  * movie-add
  * director-all
  * director-add

# Fields:

## Movie:
  * ID
  * Name
  * Year
  * director.id

## Director:
  * director.id
  * Name
  * about
  * movies

## Movie-all:
  * Name
  * Year
  * director
  * id

## Movie-add:
  * Name
  * about
  * id

## Director-all:
  * Name
  * about
  * id

## Director-add:
  * Name
  * about
  * id


# Relationships:

### Director & Movie Tables:
* The director table will have one to many relationship with the movie table. It will a one to many because a movie can have only one director, but a director can have multiple movies.

### Movie-all & Director-all Tables:
* The movie-all table will have a one to one relationship with the movie table. However, the director-all could be a one to many relationship with the movie and director tables.

### Director-add & Movie-add Tables:
The director-add table will have a one to one relationship with the director table. The movie-add table will have a one to one relationship as well with the movie table.
