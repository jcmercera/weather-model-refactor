# 🌦️ Weather Model Refactor: Fortran to Python

This project showcases the translation of a legacy **Fortran-based weather forecasting model** into modern, modular **Python** code. The goal was to maintain the original logic while improving readability, testability, and extensibility for integration into newer systems.

---

## 🧠 Purpose

Many scientific models are still written in Fortran, but maintaining or integrating them into modern workflows can be difficult. This project demonstrates how legacy algorithms can be carefully ported to Python while preserving functionality and increasing maintainability.

---

## 🔁 Original vs Refactored

| Aspect | Fortran Version | Python Version |
|--------|------------------|----------------|
| Language | FORTRAN 90 | Python 3 |
| Input/Output | Console / static files | Modular I/O handling |
| Structure | Procedural, monolithic | Modular, readable functions |
| Comments | Minimal | Fully documented |
| Testing | Manual | Easily unit-testable |

---

## 📁 Files Included

| File | Description |
|------|-------------|
| `forecast_original.f90` | Original Fortran forecasting code (if included) |
| `weather_model.py` | Fully translated Python version |
| `forecast_utils.py` | Helper functions for clarity and reuse |
| `test_inputs/` | (Optional) Sample input data files |
| `README.md` | Project documentation (this file) |

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/jcmercera/weather-model-refactor.git
   cd weather-model-refactor
