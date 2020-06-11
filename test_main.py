from urlshort import create_app

def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data

#WSGI - protocol for Python applications in order to serve website in uniform manner
#Frameworks (Flask, Django) | Servers (Gunicorn,uWSGI)
#deploying on linux server
