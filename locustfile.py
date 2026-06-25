from locust import HttpUser, task, between

class ClienteFranquia(HttpUser):
    # Tempo de 1 a 2 segundos
    wait_time = between(1, 2)

    @task
    def fazer_pedido(self):
        headers = {'Content-Type': 'application/json'}
        
        # Avisar o Locust o que vai aparecer o que é erro ou acerto
        with self.client.post("/simular_compra", json={}, headers=headers, catch_response=True) as response:
            
            # Mensagem (certo ou funcionando)
            if response.status_code == 200:
                response.success()
                
            # Mensagem (erro ou estoque esgotado)
            elif response.status_code == 400:
                response.failure("Produto esgotado (Erro de produto controlado)")
                
            # Se parar de funcionar ou cair
            else:
                response.failure(f"Erro inesperado no servidor: {response.status_code}")