# Kazakh-to-English Translator Service

This project provides a FastAPI-based RESTful service for translating text from Kazakh to English using the Hugging Face `amandyk/mt5-kazakh-english-translation` model. The service handles the model loading, caching, and provides a scalable architecture for extending the functionality to other translation models.

## Features
- **Kazakh to English Translation** using a pre-trained MT5 model.
- **FastAPI** RESTful API implementation.
- **Model Caching**: After the model is downloaded, it is cached locally for faster subsequent requests.
- **Dockerized**: Fully containerized for easy deployment on any platform.

---

## Documentation and Instructions

### a. How to Run the Application

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ExaltedA/Kaz-Eng-translator.git
    cd Kaz-Eng-translator
    ```

2. **Set Up Environment Variables**:
   - Create a `.env` file in the root of your project and specify the required environment variables:
     ```
     MODEL_NAME=amandyk/mt5-kazakh-english-translation
     LOGGING_LEVEL=INFO
     API_PORT=8000
     ```

3. **Install Dependencies**:
    If you are running it locally, create a virtual environment and install the required dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

4. **Run the Application Locally**:
    Run the application using Uvicorn (FastAPI server):
    ```bash
    python main.py
    ```

5. **Run with Docker**:
    Alternatively, you can run the application in a Docker container:

    a. **Build the Docker Image**:
    ```bash
    docker build -t translator-service .
    ```

    b. **Run the Docker Container**:
    ```bash
    docker run -p 8000:8000 translator-service
    ```

6. **Access the API**:
   The API will be accessible at `http://localhost:8000/v1/translate/`. You can test it by sending a POST request with a JSON payload containing the text you want to translate.

### Example cURL request:
```bash
curl -X POST "http://localhost:8000/v1/translate/" -H "Content-Type: application/json" -d '{"text": "Қазақстан Республикасының астанасы қай қала?"}'
```

### Health Check:
To check if the service is running properly, you can use the `/v1/healthcheck/` endpoint:
```bash
curl -X GET "http://localhost:8000/v1/healthcheck/"
```

---

### b. Technologies and Approaches

- **FastAPI**: A modern, high-performance web framework for building APIs with Python 3.7+.
- **Hugging Face Transformers**: Utilized for the Kazakh to English translation model (`amandyk/mt5-kazakh-english-translation`).
- **Pydantic**: Used for configuration management and data validation.
- **Model Caching**: The model is downloaded and cached locally after the first request, optimizing for faster responses on subsequent translations.
- **Docker**: Containerized the application for platform-independent deployment, making it easy to scale.

---

### c. Opportunities for Further Optimization and Scaling

1. **Asynchronous Model Loading**:
   - You can load the model asynchronously during startup to reduce the blocking time on startup, improving availability.

2. **Horizontal Scaling**:
   - The service can be horizontally scaled using containers, such as running multiple instances behind a load balancer to handle more traffic.

3. **Model Serving Optimization**:
   - For production environments, consider using dedicated model serving frameworks such as **TorchServe** or **Ray Serve** to efficiently distribute model inference across GPUs or clusters.

4. **Caching Translations**:
   - Implement **in-memory caching** (e.g., with Redis) to store recent translation results and minimize recomputation for frequently requested texts.

5. **Support for Multiple Language Pairs**:
   - The service can easily be extended to support more language pairs by adding new models or allowing dynamic model selection via request parameters.

---

### Project Structure

```bash
llm-integrator/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   └── translation.py    # Translation endpoint
                └── health_check.py   # Health check endpoint
│   ├── core/
│   │   └── config.py  # Application settings and configuration
│   ├── local_models/  # Cached models
│   ├── services/
│   │   └── translator.py  # Model loading and translation logic
│   │   └── interfaces/translator_interface.py  # Interface for translation service
├── tests/
│   └── test_translation.py  # Test cases for API endpoints
├── .env  # Environment variables
├── main.py  # FastAPI entry point
├── Dockerfile  # Docker configuration
├── dependencies.py  # dependency injection to create reusable instances
└── requirements.txt  # Python dependencies
```