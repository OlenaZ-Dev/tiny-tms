# 📦 Shipment Tracking API

A **Django REST Framework** project for managing customers, shipments, and tracking events.  
Supports CRUD operations and a nested endpoint for adding and retrieving shipment status updates.

---

## 🌍 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [API Endpoints](#-api-endpoints)
- [Screenshots](#-screenshots)
- [License](#-license)
- [Author](#-author)

---

## 🚀 Features
- **Customers Management** — create and manage senders/receivers.
- **Shipments Management** — track origin, destination, ETA, and status.
- **Tracking Events** — add real-time shipment status updates.
- **Nested API endpoint**: `/shipments/{id}/events`.
- Filtering, searching, and ordering for easy data retrieval.
- Automatic creation of the first tracking event when a shipment is created.

---

## 🛠 Tech Stack
- **Python 3.13**
- **Django 5.2**
- **Django REST Framework**
- SQLite (can be switched to PostgreSQL)
- DRF Browsable API for manual testing

---

## 📂 Project Structure
```
tiny-tms/
│── config/           # Project settings
│── tms/              # Main app (models, views, serializers)
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation
```bash
# Clone repository
git clone https://github.com/username/tiny-tms.git
cd tiny-tms

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```
Server will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📌 API Endpoints

### Customers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/customers/` | List customers |
| POST   | `/api/customers/` | Create customer |
| GET    | `/api/customers/{id}/` | Retrieve customer |
| PUT    | `/api/customers/{id}/` | Update customer |
| DELETE | `/api/customers/{id}/` | Delete customer |

### Shipments
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/shipments/` | List shipments |
| POST   | `/api/shipments/` | Create shipment |
| GET    | `/api/shipments/{id}/` | Retrieve shipment |
| PUT    | `/api/shipments/{id}/` | Update shipment |
| DELETE | `/api/shipments/{id}/` | Delete shipment |

### Tracking Events
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/events/` | List all tracking events |
| POST   | `/api/shipments/{id}/events/` | Add event for shipment |
| GET    | `/api/shipments/{id}/events/` | List shipment events |

---


## 📜 License
MIT License

---

## 👤 Author
Olena Zemtsova  
GitHub: [@OlenaZ-Dev](https://github.com/OlenaZ-Dev)

---

# 🇵🇱 Wersja Polska

Projekt **Django REST Framework** do zarządzania klientami, przesyłkami i zdarzeniami śledzenia.  
Obsługuje operacje CRUD oraz zagnieżdżony endpoint do dodawania i pobierania aktualizacji statusu przesyłki.

---

## 🚀 Funkcje
- **Zarządzanie klientami** — tworzenie i edytowanie nadawców/odbiorców.
- **Zarządzanie przesyłkami** — śledzenie pochodzenia, miejsca docelowego, przewidywanego czasu dostawy oraz statusu.
- **Zdarzenia śledzenia** — dodawanie aktualizacji statusu w czasie rzeczywistym.
- **Zagnieżdżony endpoint**: `/shipments/{id}/events`.
- Filtrowanie, wyszukiwanie i sortowanie danych.
- Automatyczne tworzenie pierwszego zdarzenia przy utworzeniu przesyłki.

---

## 🛠 Technologie
- **Python 3.13**
- **Django 5.2**
- **Django REST Framework**
- SQLite (można zmienić na PostgreSQL)
- DRF Browsable API do ręcznego testowania

---

## 📂 Struktura projektu
```
tiny-tms/
│── config/           # Ustawienia projektu
│── tms/              # Główna aplikacja (modele, widoki, serializery)
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Instalacja
```bash
# Klonowanie repozytorium
git clone https://github.com/username/tiny-tms.git
cd tiny-tms

# Tworzenie wirtualnego środowiska
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Instalacja zależności
pip install -r requirements.txt

# Migracje
python manage.py migrate

# Uruchomienie serwera
python manage.py runserver
```
Serwer będzie dostępny pod adresem: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📌 Endpointy API

### Klienci
| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET    | `/api/customers/` | Lista klientów |
| POST   | `/api/customers/` | Dodanie klienta |
| GET    | `/api/customers/{id}/` | Pobranie klienta |
| PUT    | `/api/customers/{id}/` | Aktualizacja klienta |
| DELETE | `/api/customers/{id}/` | Usunięcie klienta |

### Przesyłki
| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET    | `/api/shipments/` | Lista przesyłek |
| POST   | `/api/shipments/` | Dodanie przesyłki |
| GET    | `/api/shipments/{id}/` | Pobranie przesyłki |
| PUT    | `/api/shipments/{id}/` | Aktualizacja przesyłki |
| DELETE | `/api/shipments/{id}/` | Usunięcie przesyłki |

### Zdarzenia śledzenia
| Metoda | Endpoint | Opis |
|--------|----------|------|
| GET    | `/api/events/` | Lista wszystkich zdarzeń |
| POST   | `/api/shipments/{id}/events/` | Dodanie zdarzenia do przesyłki |
| GET    | `/api/shipments/{id}/events/` | Lista zdarzeń dla przesyłki |

---

## 📜 Licencja
MIT License

---

## 👤 Autor
Olena Zemtsova  
GitHub: [@OlenaZ-Dev](https://github.com/OlenaZ-Dev)
