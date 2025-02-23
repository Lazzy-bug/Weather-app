# Flask Weather App

This is a simple Flask application that fetches and displays weather information for a specified city using the OpenWeatherMap API.

## Features

- Search for weather information by city name
- Display city name, temperature, and weather condition
- Containerized using Docker
- Deployable on Kubernetes

## Prerequisites

- Python 3.8+
- Docker
- Kubernetes (optional, for deployment)

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/Lazzy-bug/Weather-app.git
    cd weather-app
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Replace the placeholder API key in `app.py` with your OpenWeatherMap API key:

    ```python
    API_KEY = 'your_openweathermap_api_key'
    ```

## Running the Application

### Locally

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

### Using Docker

1. Build the Docker image:

    ```sh
    docker build -t weather-app:latest .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 5000:5000 weather-app:latest
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000`.

### Using Kubernetes

1. Apply the Kubernetes deployment and service configurations:

    ```sh
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    ```

2. Access the application using the external IP provided by the Kubernetes service.

### Verify the deployment:

    ```sh
    kubectl get deployments
    kubectl get pods
    kubectl get svc
    ```

### Access the service:

    ```sh
    minikube service weather-app-service
    ```

## File Structure

```
/weather-app
│
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── deployment.yaml         # Kubernetes deployment configuration
├── service.yaml            # Kubernetes service configuration
├── templates/
│   └── index.html          # HTML template
└── static/
    └── style.css           # CSS styles
```

## License

This project is licensed under the MIT License.
