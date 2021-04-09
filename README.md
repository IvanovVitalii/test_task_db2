# Django application - public chat room(only RESTful API).

Unauthenticated users can post messages via API in chat so others can read them.
Messages need to be saved to the database.

## Basic requirements:

- [x] Django, Django REST Framework, PostgreSQL
- [x] The message must contain author(unauthenticated user) email and text, create date and update date.
- [x] Email validation (regex to check if that is real email)
- [ ] Message validation (regex to check if message is not empty string, and length < 100)

## API methods:

- [x] GET method for getting all messages with pagination by 10 messages per request.
e.g.
/api/messages/list/0 will return first 10 messages
/api/messages/list/1 will return second 10 messages
etc
- [x] GET method for getting single message by unique identifier
e.g.
/api/messages/single/123
- [x] POST method for creating a new message
Body accepts email and text.
- [ ] Add request validators
- [ ] API documentation(preferably with sandbox for sending requests, e.g. Swagger)
- [ ] Deploy to Heroku

## Advanced requirements:

- [ ] Continuous integration CircleCI / TravisCI
- [ ] Deploy to AWS / DigitalOcean
