# ALX Travel App – 0x00 Database Modeling & Data Seeding

## Objective
This project implements database models, serializers, and a data seeder for the `alx_travel_app_0x00` project.

---


---

## 📌 Models Implemented

### 1. Listing
Fields:
- title  
- description  
- price_per_night  
- location  
- max_guests  
- created_at  

### 2. Booking
Fields:
- listing (FK)  
- guest_name  
- guest_email  
- check_in  
- check_out  
- total_price  

### 3. Review
Fields:
- listing (FK)  
- reviewer_name  
- rating (1–5 range)  
- comment  

---

## 📌 Serializers
Created in `listings/serializers.py` for:
- ListingSerializer  
- BookingSerializer  

---

## 📌 Seeder Command

### Run Seeder:

```bash
python manage.py seed
