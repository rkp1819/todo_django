from django.test import TestCase

# Create your tests here.

class TodoViewSetTests(TestCase):

    def test_get_all_todos(self):
        response = self.client.get('/todos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_create_todo(self):
        response = self.client.post('/todos/', {'title': 'Test Todo', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], 'Test Todo')

    def test_get_completed_todos(self):
        response = self.client.get('/todos/completed/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

    def test_get_pending_todos(self):
        response = self.client.get('/todos/pending/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
        
    def test_search_todos(self):
        response = self.client.get('/todos/?search=Test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_update_todo(self):
        response = self.client.put('/todos/1/', {'title': 'Updated Todo', 'description': 'Updated Description'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Updated Todo')
    
    def test_delete_todo(self):
        response = self.client.delete('/todos/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(response.data), 0)
        
    def test_get_todo_by_id(self):
        response = self.client.get('/todos/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Todo')

    def test_get_todo_by_id_not_found(self):
        response = self.client.get('/todos/999/')
        self.assertEqual(response.status_code, 404)
    
    def test_get_todo_by_id_invalid_id(self):
        response = self.client.get('/todos/invalid_id/')
        self.assertEqual(response.status_code, 404)
        
    def test_get_todo_by_id_empty_id(self):
        response = self.client.get('/todos//')
        self.assertEqual(response.status_code, 404)
        
        
    