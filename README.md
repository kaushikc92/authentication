# authentication

1. Run this server on a url. Say, 0.0.0.0:8000
2. Run a client application on a url. Say, 0.0.0.0:8001
3. Create admin user
4. Create a normal user
5. Login at /admin
6. Go to /o/applications/ and register the application. Client type: public, Authorization grant type: authorization code, and specify redirect uri
7. Go to /o/authorize/?response_type=code&client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&state=1234xyz
8. Login as normal user and click on authorize in the prompt.
9. You will be redirected to REDIRECT_URI/?code=CODE
10. Make POST request to o/token/ with following data grant_type=authorization_code, code=CODE, redirect_uri=REDIRECT_URI, client_id=CLIENT_ID, client_secret=CLIENT_SECRET 
