# consumer_affairs_cc
consumer affairs coding challenge.

Considering that i do not have much information about the apps running or the websites beign served i will implement a rest API usind the Django Rest Framework.
I will authenticate the apps using tokens and will receive their data and store it in model, this model will contain a boolean to indicate if the data has been validated.
By default the data will not be validated, another process will be scheduled to run and validate data in a periodic manner, this validator will log any errors encountered and flag the event as validated or not depending on the result of the validation.

API Documentation:

https://documenter.getpostman.com/view/18353863/UVJYJyRh
