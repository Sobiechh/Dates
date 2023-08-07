# FastAPI Dates API

This is a simple REST API built using FastAPI that interacts with an external API to provide fun facts about dates. It allows you to store and retrieve dates along with their fun facts.

## Getting Started

### Prerequisites

- Python 3.7
- Pip (Python package manager)
- Deta Space account (for deployment)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-fastapi-dates-app.git
cd your-fastapi-dates-app
```
Install the required packages:

pip install -r requirements.txt
Create a .env file in the project root directory and set your environment variables:

```dotenv
POSTGRES_DB=your_postgres_db
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_HOST=your_postgres_host
SECRET_API_KEY=your_secret_api_key
```

### Usage
Run the FastAPI application:

```
uvicorn main:app --host 0.0.0.0 --port 8000
```
Access the API documentation at: http://localhost:8000/docs

### Demo
You can check out the live demo of this application here: https://datessppiotr.onrender.com/docs

### Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.