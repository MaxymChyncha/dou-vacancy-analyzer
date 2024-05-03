tools = [
    "GIT",
    "SQL",
    "REST",
    "API",
    "docker",
    "AWS",
    "GCP",
    "Linux",
    "Django",
    "Postgresql",
    "Artificial Intelligence",
    "AI",
    "JS",
    "JavaScript"
    "machine learning",
    "ML",
    "react",
    "OOP",
    "Flask",
    "NoSQL",
    "SQL",
    "Sqlite",
    "backend",
    "fullstack",
    "microservice",
    "MongoDB",
    "HTML",
    "CSS",
    "algorithms",
    "DRF",
    "Django REST",
    "FastAPI",
    "asyncio",
    "Graphql",
    "Pytest",
    "Unitest",
    "Celery",
    "Redis",
    "Math",
    "Data Structures",
    "Statistics",
    "Selenium",
    "Scrapy",
    "ООП",
    "gRPC",
    "TCP",
    "parsing",
    "threading",
    "multiprocess",
    "Node",
    "SOLID",
    "Odoo",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "SciPy",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Scikit-learn",
    "Alembic"
]


def extract_technologies(description: str) -> list:
    return list(
        set(
            [
                tool
                for tool in tools
                if tool.lower() in description.lower()
            ]
        )
    )
