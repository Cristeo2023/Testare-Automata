'''
Folosim https://jsonplaceholder.typicode.com/guide/ Toate requesturile se vor face prima data in Postman
(pentru verificare), iar apoi folosind libraria requests din Python.

Structura datelor este următoarea:
- fiecare post este deținut de un user, și poate avea mai multe comments
- fiecare album este deținut de un user, și poate avea mai multe photos
- fiecare todo este detinut de un user.
'''

'''
1. Alege un user din lista de useri predefiniti. Pentru acesta, fa requesturile necesare pentru a afișa următoarele
informații:
	-> lista de albume
	-> lista de todos
Pentru a menține output-ul la un nivel acceptabil, afișează la fiecare dintre aceste liste doar informații despre
primele 3 obiecte, iar apoi afiseaza "+x more albums/todos", unde x este numărul de obiecte rămase
'''
import requests
from pprint import pprint


class APIEx:
    URL = 'https://jsonplaceholder.typicode.com/'

    def get_album_list(self, userId):
        response = requests.get(f'{self.URL}/albums?userId = {userId} ')
        album = response.json()
        first_three = album[:3]
        return first_three, len(album) - 3

    def get_todo_list(self, userId):
        response = requests.get(f'{self.URL}/todos?userId = {userId}')
        todos = response.json()
        first_three = todos[:3]
        return first_three, len(todos) - 3

    '''
    2. Alege un post, și afișează lista de comentarii. Alege un album, si afiseaza lista de photos.
    '''

    def get_comments_list(self, postId):
        response = requests.get(f'{self.URL}/comments?postId = {postId}')
        return response.json()

    def get_photos(self, albumId):
        response = requests.get(f'{self.URL}/photos?albumId = {albumId}')
        return response.json()

    '''
    3. Creeaza post și adaugă un albums nou (atentie, acesta NU va fi salvat, dar putem analiza răspunsul pentru a vedea
    cum ar arata în viitor dacă ar fi fost salvat). Încearcă să-l creezi cu si fără id. Ce observi?
    '''

    def create_post(self, new_post):
        response = requests.post(f'{self.URL}/albums', json=new_post)
        return response.json()

    '''
    4. Alege un todos existent și realizează operațiunile de PUT si PATCH (atentie, modificările NU vor fi salvate,
    analizăm doar răspunsul). Ce observi ca este diferit între cele 2 metode?
    '''
    def put_todos(self,new_post):
        response = requests.put(f'{self.URL}/todos/1', json=new_post)
        return response.json()

    def patch_todos(self,new_post):
        response = requests.patch(f'{self.URL}/todos/1', json=new_post)
        return response.json()

    '''
    5. Alege un album, și ia pozele din acesta în 2 moduri diferite (o data cu nested resource, o data folosind query
    params). Verifica dacă exista vreo diferenta intre cele 2 rezultate.
    '''
    def get_nested_resource(self,albumId):
        response = requests.get(f'{self.URL}/albums/{albumId}/photos')
        return response.json()

    def get_query_param(self,albumId):
        response = requests.get(f'{self.URL}/photos?albumId={albumId}')
        return response.json()


print('Ex 1.')
client = APIEx()
album, left = client.get_album_list(1)
pprint(album)
print(f'+{left} more albums')
todos, left = client.get_todo_list(1)
pprint(todos)
print(f'+{left} more todos')

print('Ex2')
pprint(client.get_comments_list(1))
pprint(client.get_photos(1))

print('Ex 3.')
payload = {
    "userId": '9',
    "title": "album nou"
}
pprint(client.create_post(payload))

print('Ex 4.')
payload = {
    "title": "Todos nou"
}
print('PUT')
pprint(client.put_todos(payload))
print('PATCH')
pprint(client.patch_todos(payload))

print('Ex 5.')
print('Cu NESTED')
pprint(client.get_nested_resource(3))
print('Cu QUERY')
pprint(client.get_query_param(3))

if client.get_nested_resource(3) == client.get_query_param(3):
    print('Rezultatele sunt la fel')
else:
    print('Exista diferente intre rezultate')