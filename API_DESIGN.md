# API Design Documentation

## Overview
This API provides functionality for managing travel-related data and operations.

## Base URL
```
`https://api.raja-travel.com/v1`
```

## Authentication
- Use Bearer Token for authentication.
- Include the token in the Authorization header for all requests.

## Endpoints

### 1. User Authentication
- **Method**: POST
- **Endpoint**: `/auth/login`
- **Description**: Authenticates a user and returns a token.
- **Request**:
  - Body:
    - `username`: string
    - `password`: string
- **Response**:
  - 200 OK: `{ "token": "your_auth_token" }`
  - 401 Unauthorized: `{ "message": "Invalid credentials" }`

### 2. Get All Trips
- **Method**: GET
- **Endpoint**: `/trips`
- **Description**: Retrieves all trips for the authenticated user.
- **Response**:
  - 200 OK: `[ { "id": 1, "destination": "Paris", ... }, ... ]`

### 3. Create a New Trip
- **Method**: POST
- **Endpoint**: `/trips`
- **Description**: Creates a new trip.
- **Request**:
  - Body:
    - `destination`: string
    - `date`: string (YYYY-MM-DD)
- **Response**:
  - 201 Created: `{ "id": 1, "destination": "Paris", ... }`

### 4. Update Trip
- **Method**: PUT
- **Endpoint**: `/trips/{id}`
- **Description**: Updates an existing trip.
- **Request**:
  - Body:
    - `destination`: string
    - `date`: string (YYYY-MM-DD)
- **Response**:
  - 200 OK: `{ "id": 1, "destination": "Paris", ... }`

### 5. Delete Trip
- **Method**: DELETE
- **Endpoint**: `/trips/{id}`
- **Description**: Deletes a trip.
- **Response**:
  - 204 No Content
