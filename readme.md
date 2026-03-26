# ECO_RIDE
* A Python-based project focused on providing an **eco-friendly ride application / toolkit**. This repository includes the core application code, test suite, dependency specifications, and any models or utilities needed for development and experimentation.
---
## Project Overview
* **ECO_RIDE** is designed to offer a structured codebase for building eco-conscious ride sharing, routing, or ride optimization features (e.g., to reduce emissions or encourage shared transport).  
The repository is structured to support:

- Core application logic under `src/`
- Testing under `tests/`
- Dependency list in `requirements`
- Scalable expansion for models and utilities

---

## Project Structure

```plaintext
ECO_RIDE/
├── .idea/                         # IDE configuration files
├── requirements.txt              # Python dependencies
├── src/                           # Main application source code
│   ├── __init__.py
│   │
│   ├── EcoRideMain.py            # Application entry point (Console UI)
│   │
│   ├── fleet/                    # Fleet management logic
│   │   ├── __init__.py
│   │   ├── hub.py
│   │   └── hub_manager.py
│   │
│   ├── models/                   # Core domain models
│   │   ├── __init__.py
│   │   ├── vehicle.py
│   │   ├── electric_car.py
│   │   └── electric_scooter.py
│   │
│   ├── helper/                   # Shared utilities
│   │   ├── __init__.py
│   │   │
│   │   ├── enums/                # Enum definitions
│   │   │   ├── __init__.py
│   │   │   └── vehicle_status.py
│   │   │
│   │   ├── exceptions/           # Custom exceptions
│   │   │   ├── __init__.py
│   │   │   ├── battery_level.py
│   │   │   ├── rental_price.py
│   │   │   └── vehicle_exists.py
│   │   │
│   │   └── io_utils/             # File handling utilities
│   │       ├── __init__.py
│   │       ├── csv_writer.py
│   │       └── json_writer.py
│   │
│   ├── fleet_data.json           # JSON persistence file
│   └── vehicle_data.csv          # CSV persistence file
│
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_exception_units.py
│   ├── test_hub_manager_units.py
│
└── README.md
```
## Installation & Setup
```commandline
    git clone https://github.com/DEBDEEPTA/ECO_RIDE.git
    cd ECO_RIDE
```
## Create Virtual Environment
```commandline
    python -m venv .venv
```
## Activate Virtual Enviroment
* <u>_Windows_</u>
```commandline
   .venv\Scripts\activate
```
* <u>_Mac/Linux_</u>
```commandline
   source .venv/bin/activate
```
## Install Dependencies
```commandline
    pip install -r requirements.txt
```
## Running the Application
```commandline
    python src/EcoRideMain.py
```