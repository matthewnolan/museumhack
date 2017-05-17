https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django

https://fezvrasta.github.io/bootstrap-material-design/#getting-started

https://devcenter.heroku.com/articles/heroku-postgres-backups

Notes:

5/8/17: I imported new data to museum_db5 which may not be formatted property. May have to revert back to old db (museum_db4), and re-import data


To Import a new CSV.

1. Export as a CSV
2. Copy to imported_data
3. backup existing db in case of import error. If there is an error with even one row, it will be hard to know where you left off. Its easier to revert to a previous state and try again.
	- to backup enter pswl command line: $ psql
	- CREATE DATABASE newdb WITH TEMPLATE originaldb OWNER dbuser;

4. then run import script

5. if all is good, push this data to heroku. 
	- $ heroku pg:reset museumhack::DATABASE_URL
	- $ heroku pg:push museum_db5 museumhack::DATABASE_URL --app museumhack