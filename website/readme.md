### Initialization

1. Install Poetry if not installed
2. run "Poetry install"
3. run "Poetry run django migrate"
4. run "Poetry run django createsuperuser"
5. create .env file
.env structure
```
DATABASE_NAME=string
DATABASE_USER=string
DATABASE_PASSWORD=string
DATABASE_HOST=string
DATABASE_PORT=string
SITE_ID =int
SOLR_URL=string

```
*Only postgress db is allowed
6. Goto sites and create a site Follow this link: https://www.section.io/engineering-education/django-google-oauth/
7. You will find site id in sties section
To Run application "Poetry run server"