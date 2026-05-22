# 🚲 Bike Log Pro

O **Bike Log Pro** é o sistema de gestão de manutenção preventiva para ciclistas que levam a sério a performance e a durabilidade do seu equipamento.

Desenvolvido para eliminar o "achismo" na hora de trocar componentes, o projeto centraliza o histórico de uso e revisões, garantindo que você saiba exatamente quantos quilômetros cada peça rodou e quando é o momento ideal para uma manutenção — evitando surpresas desagradáveis no meio da trilha.

---

## 🛠️ Stack Tecnológica
*   **Backend:** Python 3.12 + Django Framework
*   **API:** Django Rest Framework
*   **Banco de Dados:** PostgreSQL
*   **Containers:** Docker & Docker Compose
*   **Gerenciamento:** PDM (Python Dependency Manager)

---

## 🚀 Funcionalidades Atuais
- [x] **Gestão de Bikes:** Cadastro e organização da sua frota.
- [x] **Componentização:** Acompanhamento individual de peças (Freios, Transmissão, Suspensão, etc.).
- [x] **Histórico de Manutenção:** Registro detalhado de revisões, custos e quilometragem no momento do serviço.
- [x] **API REST:** Endpoints prontos para integração com front-ends mobile ou web.
- [x] **Painel Administrativo:** Interface completa para gestão de dados via Django Admin.

## 🔜 Roadmap (Futuras Features)
- [ ] **Alerta de Manutenção:** Lógica inteligente para notificar quando um componente atingir o limite de uso.
- [ ] **Integração com Strava/GPS:** Importação automática de logs de pedal para atualização de quilometragem.
- [ ] **Dashboard Financeiro:** Relatório de gastos mensais/anuais com manutenção de bike.
- [ ] **App Mobile:** Interface dedicada para acesso rápido na oficina.

---

## ⚙️ Como usar

### Pré-requisitos
- Ter o **Docker** e **Docker Compose** instalados na sua máquina.

### Instalação
1. Clone o repositório:
   
```bash
   git clone https://github.com/mklamaral/bike_log_v2.git
   cd bike_log_v2

```

2. Suba a infraestrutura completa:

```bash
   docker compose up -d --build

```

3. Aplique as migrações no banco de dados:

```bash
   docker compose exec api python manage.py migrate

```

4. Crie seu usuário administrador:

```bash
   docker compose exec api python manage.py createsuperuser

```

5. Acesse o sistema:
* **Admin:** `http://localhost:19003/admin`
* **API:** `http://localhost:19003/api/`



---

## 🤝 Contribuição

Este projeto é de uso pessoal, mas feedbacks e sugestões de melhoria são sempre bem-vindos. Se você também é um "mecânico de quintal" e quer adicionar uma funcionalidade, sinta-se à vontade para abrir uma *Issue* ou *Pull Request*.

---

*Desenvolvido por Mikael Amaral - Sistemas de Informação IFC Araquari.*