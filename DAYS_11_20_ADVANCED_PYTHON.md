# 🚀 10 More Days Python Series: Days 11-20 (Advanced Level)

**Level:** Advanced | **Duration:** 10 Days (30-40 hours)

After completing Days 1-10, you've mastered Python fundamentals and intermediate concepts. Now it's time to level up! Days 11-20 cover advanced Python topics, web development, data science basics, and real-world project development.

---

## 📋 Course Overview

This advanced 10-day series builds upon your foundation with:

✅ Advanced OOP patterns and design patterns
✅ Web development with Flask and Django
✅ Data analysis and visualization
✅ APIs and web scraping
✅ Database management
✅ Testing and performance optimization
✅ Deployment and DevOps basics
✅ Machine learning introduction
✅ Advanced Python packages
✅ Production-ready projects

---

## 🗓️ Day-by-Day Breakdown

---

### **Day 11: Advanced OOP Patterns & Design Patterns**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Singleton pattern
- Factory pattern
- Observer pattern
- Strategy pattern
- Decorator pattern (advanced)
- Abstract Base Classes (ABC)
- Metaclasses
- Context managers (advanced)

**Hands-on Exercise:**

```python
# Exercise: Implementing Design Patterns

# 1. Singleton Pattern
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. Factory Pattern
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            'dog': Dog,
            'cat': Cat,
            'bird': Bird
        }
        return animals.get(animal_type, Dog)()

# 3. Observer Pattern
class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Observer received: {message}")

# 4. Decorator Pattern (Advanced)
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

# Usage
print(slow_function())

# 5. Abstract Base Classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car started"
    
    def stop(self):
        return "Car stopped"
```

**Resources:**
- Design Patterns in Python: https://refactoring.guru/design-patterns/python
- Real Python Design Patterns: https://realpython.com/

---

### **Day 12: Web Development with Flask (Part 1)**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Flask basics and routing
- Request/response handling
- Templates with Jinja2
- Static files management
- Blueprints for modular apps
- Error handling in web apps

**Hands-on Exercise:**

```python
# Exercise: Building a Flask Web Application

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database (temporary)
tasks = []

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        data = request.get_json()
        task = {
            'id': len(tasks) + 1,
            'title': data.get('title'),
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        tasks.append(task)
        return jsonify(task), 201
    return jsonify(tasks)

@app.route('/api/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task_detail(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    
    if request.method == 'GET':
        return jsonify(task)
    elif request.method == 'PUT':
        data = request.get_json()
        task.update(data)
        return jsonify(task)
    elif request.method == 'DELETE':
        tasks.remove(task)
        return '', 204

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

**Setup:**
```bash
pip install flask
python app.py
```

**Resources:**
- Flask Official: https://flask.palletsprojects.com/
- Miguel Grinberg's Flask Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

---

### **Day 13: Web Development with Flask (Part 2) & Databases**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Flask SQLAlchemy ORM
- Database models
- Relationships (One-to-Many, Many-to-Many)
- Database migrations with Alembic
- Query optimization
- Authentication basics

**Hands-on Exercise:**

```python
# Exercise: Flask with SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<Post {self.title}>'

# Routes
@app.route('/create_db')
def create_db():
    with app.app_context():
        db.create_all()
    return 'Database created!'

@app.route('/add_user')
def add_user():
    user = User(
        username='john_doe',
        email='john@example.com',
        password_hash='hashed_password'
    )
    db.session.add(user)
    db.session.commit()
    return f'User {user.username} created!'

@app.route('/users')
def get_users():
    users = User.query.all()
    return [{
        'id': u.id,
        'username': u.username,
        'email': u.email,
        'posts': len(u.posts)
    } for u in users]

if __name__ == '__main__':
    app.run(debug=True)
```

**Resources:**
- SQLAlchemy: https://docs.sqlalchemy.org/
- Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/

---

### **Day 14: REST APIs & Web Scraping**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- RESTful API design principles
- Status codes and HTTP methods
- Request validation
- Response formatting
- Web scraping with BeautifulSoup
- Handling requests and responses
- Error handling in APIs

**Hands-on Exercise:**

```python
# Exercise: REST API & Web Scraping

import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Example 1: Consuming REST API
@app.route('/weather/<city>')
def get_weather(city):
    url = f'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 40.7128,
        'longitude': -74.0060,
        'current': 'temperature'
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch weather'}), 500

# Example 2: Web Scraping
def scrape_news():
    url = 'https://example-news-site.com'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        
        for article in soup.find_all('article', limit=5):
            title = article.find('h2').text
            summary = article.find('p').text
            articles.append({
                'title': title,
                'summary': summary
            })
        
        return articles
    except requests.RequestException as e:
        print(f"Error scraping: {e}")
        return []

@app.route('/news')
def get_news():
    articles = scrape_news()
    return jsonify(articles)

# Example 3: Simple REST API
users_db = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}
]

@app.route('/api/users', methods=['GET'])
def list_users():
    return jsonify(users_db), 200

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users_db if u['id'] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        'id': max(u['id'] for u in users_db) + 1,
        'name': data.get('name'),
        'email': data.get('email')
    }
    users_db.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
```

**Installation:**
```bash
pip install requests beautifulsoup4
```

**Resources:**
- REST API Best Practices: https://restfulapi.net/
- BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/
- Requests: https://requests.readthedocs.io/

---

### **Day 15: Data Analysis with Pandas & Visualization**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- DataFrames and Series
- Data cleaning and transformation
- Grouping and aggregation
- Merging and joining data
- Data visualization with Matplotlib/Seaborn
- Statistical analysis
- Time series data

**Hands-on Exercise:**

```python
# Exercise: Data Analysis with Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create and explore data
data = {
    'Date': pd.date_range('2026-01-01', periods=100),
    'Product': np.random.choice(['A', 'B', 'C'], 100),
    'Sales': np.random.randint(100, 1000, 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
}

df = pd.DataFrame(data)

# 2. Data exploration
print(df.head())
print(df.info())
print(df.describe())

# 3. Data cleaning
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df = df.drop_duplicates()

# 4. Data transformation
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# 5. Grouping and aggregation
sales_by_product = df.groupby('Product')['Sales'].sum()
sales_by_region = df.groupby('Region')['Sales'].agg(['sum', 'mean', 'count'])

# 6. Filtering
high_sales = df[df['Sales'] > 500]

# 7. Data visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Sales by product
df.groupby('Product')['Sales'].sum().plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Sales by Product')

# Plot 2: Sales over time
df.set_index('Date')['Sales'].plot(ax=axes[0, 1])
axes[0, 1].set_title('Sales Over Time')

# Plot 3: Distribution of sales
axes[1, 0].hist(df['Sales'], bins=20)
axes[1, 0].set_title('Sales Distribution')

# Plot 4: Sales by region
df.boxplot(column='Sales', by='Region', ax=axes[1, 1])
axes[1, 1].set_title('Sales by Region')

plt.tight_layout()
plt.show()

# 8. Statistical analysis
correlation = df[['Sales']].corr()
print(correlation)

# 9. Pivot tables
pivot = df.pivot_table(values='Sales', index='Product', columns='Region', aggfunc='sum')
print(pivot)
```

**Installation:**
```bash
pip install pandas numpy matplotlib seaborn
```

**Resources:**
- Pandas Documentation: https://pandas.pydata.org/
- Matplotlib: https://matplotlib.org/
- Seaborn: https://seaborn.pydata.org/

---

### **Day 16: Testing & Code Quality**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Unit testing with unittest
- Testing with pytest
- Test fixtures and mocking
- Test coverage
- Integration testing
- Code quality tools (pylint, flake8)
- Documentation testing
- Continuous Integration basics

**Hands-on Exercise:**

```python
# Exercise: Testing and Code Quality

import unittest
from unittest.mock import patch, MagicMock

# Code to test
def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, operation, a, b):
        result = operation(a, b)
        self.history.append((operation.__name__, a, b, result))
        return result

# Unit Tests
class TestMathFunctions(unittest.TestCase):
    """Test mathematical functions"""
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(1, 3), 0.333, places=2)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestCalculator(unittest.TestCase):
    """Test Calculator class"""
    
    def setUp(self):
        """Create a calculator instance before each test"""
        self.calc = Calculator()
    
    def test_calculate_with_add(self):
        result = self.calc.calculate(add, 5, 3)
        self.assertEqual(result, 8)
        self.assertEqual(len(self.calc.history), 1)
    
    def test_history(self):
        self.calc.calculate(add, 2, 3)
        self.calc.calculate(multiply, 4, 5)
        self.assertEqual(len(self.calc.history), 2)
        self.assertEqual(self.calc.history[0][0], 'add')

# Parametrized tests
class TestParametrized(unittest.TestCase):
    """Parametrized tests"""
    
    def test_operations(self):
        test_cases = [
            (add, 2, 3, 5),
            (add, -1, 1, 0),
            (multiply, 3, 4, 12),
            (divide, 10, 2, 5)
        ]
        
        for operation, a, b, expected in test_cases:
            with self.subTest(operation=operation.__name__, a=a, b=b):
                result = operation(a, b)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
```

**Run tests:**
```bash
# Run all tests
python -m unittest discover

# Run specific test file
python -m unittest test_calculator

# Run with coverage
pip install coverage
coverage run -m unittest discover
coverage report
coverage html
```

**Resources:**
- unittest Documentation: https://docs.python.org/3/library/unittest.html
- pytest: https://docs.pytest.org/
- Code Quality Tools: https://www.python.org/dev/peps/pep-0008/

---

### **Day 17: Performance Optimization & Profiling**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Profiling code with cProfile
- Memory profiling
- Optimization techniques
- Algorithm efficiency (Big O notation)
- Caching and memoization
- Multithreading and multiprocessing
- Async programming basics

**Hands-on Exercise:**

```python
# Exercise: Performance Optimization

import cProfile
import pstats
import io
import time
from functools import lru_cache
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 1. Basic profiling
def fibonacci_slow(n):
    if n < 2:
        return n
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# With memoization (optimization)
@lru_cache(maxsize=None)
def fibonacci_fast(n):
    if n < 2:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# Profiling comparison
def profile_fibonacci():
    pr = cProfile.Profile()
    
    print("Slow version:")
    pr.enable()
    result_slow = fibonacci_slow(30)
    pr.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())
    
    print("\nFast version:")
    pr.enable()
    result_fast = fibonacci_fast(30)
    pr.disable()
    
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()
    print(s.getvalue())

# 2. Memory profiling
import sys

def memory_test():
    small_list = [i for i in range(100)]
    large_list = [i for i in range(1000000)]
    
    print(f"Small list size: {sys.getsizeof(small_list)} bytes")
    print(f"Large list size: {sys.getsizeof(large_list)} bytes")

# 3. Timing execution
def timing_example():
    start = time.time()
    result = fibonacci_fast(30)
    end = time.time()
    print(f"Execution time: {end - start:.4f} seconds")

# 4. Multithreading
def worker(name, delay):
    print(f"Worker {name} starting")
    time.sleep(delay)
    print(f"Worker {name} done")

def threading_example():
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"T{i}", 1))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

# 5. Thread pool
def cpu_bound_task(n):
    return sum(i for i in range(n))

def thread_pool_example():
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, [1000000, 2000000, 3000000]))
    return results

# 6. Async programming
import asyncio

async def async_task(name, delay):
    print(f"Task {name} starting")
    await asyncio.sleep(delay)
    print(f"Task {name} done")
    return f"{name} result"

async def async_example():
    tasks = [async_task(f"T{i}", 1) for i in range(3)]
    results = await asyncio.gather(*tasks)
    return results

if __name__ == '__main__':
    print("=== Profiling ===")
    profile_fibonacci()
    
    print("\n=== Memory ===")
    memory_test()
    
    print("\n=== Timing ===")
    timing_example()
    
    print("\n=== Threading ===")
    threading_example()
    
    print("\n=== Thread Pool ===")
    thread_pool_example()
    
    print("\n=== Async ===")
    asyncio.run(async_example())
```

**Resources:**
- cProfile: https://docs.python.org/3/library/profile.html
- Optimization Guide: https://realpython.com/python-performance/
- Async: https://docs.python.org/3/library/asyncio.html

---

### **Day 18: Deployment & DevOps Basics**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Docker basics
- Docker containers
- Docker Compose
- Environment management
- Configuration management
- Deploying to cloud (Heroku, AWS basics)
- CI/CD pipelines
- Logging and monitoring

**Hands-on Exercise:**

```dockerfile
# Dockerfile Example
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - DATABASE_URL=postgresql://user:pass@db:5432/appdb
    depends_on:
      - db
  
  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=appdb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

```bash
# Build and run
docker build -t myapp .
docker run -p 5000:5000 myapp

# Docker Compose
docker-compose up
docker-compose down
```

**Resources:**
- Docker Documentation: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- Deployment Guide: https://realpython.com/flask-deployment/

---

### **Day 19: Introduction to Machine Learning**
**Duration:** 3-4 hours | **Level:** Advanced

**Topics:**
- Machine Learning basics
- Supervised vs Unsupervised learning
- Scikit-learn introduction
- Data preprocessing
- Model training and evaluation
- Classification example
- Regression example
- Cross-validation

**Hands-on Exercise:**

```python
# Exercise: Simple Machine Learning Model

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import numpy as np

# 1. Load data
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Preprocess data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 5. Make predictions
y_pred = model.predict(X_test_scaled)

# 6. Evaluate model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# 7. Cross-validation
cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
print(f"Cross-validation scores: {cv_scores}")
print(f"Average CV score: {cv_scores.mean():.4f}")

# 8. Feature importance
feature_importance = model.feature_importances_
for name, importance in zip(iris.feature_names, feature_importance):
    print(f"{name}: {importance:.4f}")
```

**Installation:**
```bash
pip install scikit-learn
```

**Resources:**
- Scikit-learn: https://scikit-learn.org/
- ML Basics: https://developers.google.com/machine-learning/crash-course
- Real Python ML: https://realpython.com/

---

### **Day 20: Capstone Project - Production-Ready Application**
**Duration:** 5-6 hours | **Level:** Advanced

**Project:** Build a complete production-ready application that combines everything you've learned!

**Project Requirements:**

1. **Backend (Flask/Django)**
   - REST API endpoints
   - Database with SQLAlchemy
   - Authentication/Authorization
   - Error handling
   - Logging

2. **Data Processing**
   - Data analysis with Pandas
   - Data visualization
   - Statistical analysis

3. **Testing**
   - Unit tests
   - Integration tests
   - Test coverage > 80%

4. **Deployment**
   - Docker containerization
   - Docker Compose setup
   - Environment configuration

5. **Documentation**
   - API documentation
   - Setup instructions
   - Code comments

**Hands-on Exercise - Project: Data Analysis Dashboard**

```python
# app.py - Main Flask Application

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

# Configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///analytics.db'
CORS(app)
db = SQLAlchemy(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Models
class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    value = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.isoformat(),
            'value': self.value,
            'category': self.category
        }

# Routes
@app.route('/api/data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()
        point = DataPoint(
            value=data.get('value'),
            category=data.get('category')
        )
        db.session.add(point)
        db.session.commit()
        logger.info(f"Added data point: {point.to_dict()}")
        return jsonify(point.to_dict()), 201
    except Exception as e:
        logger.error(f"Error adding data: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        days = request.args.get('days', 7, type=int)
        start_date = datetime.utcnow() - timedelta(days=days)
        
        data = DataPoint.query.filter(
            DataPoint.timestamp >= start_date
        ).all()
        
        return jsonify([d.to_dict() for d in data]), 200
    except Exception as e:
        logger.error(f"Error getting data: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    try:
        days = request.args.get('days', 7, type=int)
        start_date = datetime.utcnow() - timedelta(days=days)
        
        data = DataPoint.query.filter(
            DataPoint.timestamp >= start_date
        ).all()
        
        values = [d.value for d in data]
        
        stats = {
            'count': len(values),
            'mean': float(np.mean(values)) if values else 0,
            'median': float(np.median(values)) if values else 0,
            'std': float(np.std(values)) if values else 0,
            'min': float(min(values)) if values else 0,
            'max': float(max(values)) if values else 0
        }
        
        return jsonify(stats), 200
    except Exception as e:
        logger.error(f"Error getting statistics: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/trends', methods=['GET'])
def get_trends():
    try:
        days = request.args.get('days', 30, type=int)
        start_date = datetime.utcnow() - timedelta(days=days)
        
        data = DataPoint.query.filter(
            DataPoint.timestamp >= start_date
        ).all()
        
        # Convert to DataFrame
        df = pd.DataFrame([{
            'timestamp': d.timestamp,
            'value': d.value,
            'category': d.category
        } for d in data])
        
        if df.empty:
            return jsonify({'trend': 'No data available'}), 200
        
        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        daily_trend = df.groupby('date')['value'].mean()
        
        return jsonify({
            'dates': [str(d) for d in daily_trend.index],
            'values': daily_trend.values.tolist()
        }), 200
    except Exception as e:
        logger.error(f"Error getting trends: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    logger.error(f"Server error: {str(error)}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# test_app.py - Tests

import unittest
import json
from app import app, db, DataPoint

class TestDataAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        
        with app.app_context():
            db.create_all()
    
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
    
    def test_add_data(self):
        response = self.client.post('/api/data', json={
            'value': 100,
            'category': 'test'
        })
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['value'], 100)
    
    def test_get_data(self):
        self.client.post('/api/data', json={
            'value': 100,
            'category': 'test'
        })
        response = self.client.get('/api/data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)

if __name__ == '__main__':
    unittest.main()
```

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

```bash
# requirements.txt
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Flask-CORS==3.0.10
pandas==1.3.0
numpy==1.21.0
gunicorn==20.1.0
```

**Resources:**
- Full Stack Python: https://www.fullstackpython.com/
- Flask by Example: https://realpython.com/

---

## 🏆 Capstone Project Checklist

- [ ] Backend API with 5+ endpoints
- [ ] Database with relationships
- [ ] Authentication (optional)
- [ ] Data processing and analysis
- [ ] Unit tests (>80% coverage)
- [ ] Integration tests
- [ ] Error handling and logging
- [ ] Docker containerization
- [ ] Documentation (README, API docs)
- [ ] Deployment ready

---

## 📚 Next Steps After Days 11-20

### **Advanced Topics**
- 🎯 FastAPI (modern web framework)
- 🎯 GraphQL with Python
- 🎯 Microservices architecture
- 🎯 Message queues (Celery, RabbitMQ)
- 🎯 Advanced ML (Deep Learning, NLP)

### **Specialization Paths**
- **Web Developer**: Django + Nginx + PostgreSQL
- **Data Scientist**: NumPy + Pandas + Scikit-learn + TensorFlow
- **DevOps Engineer**: Docker + Kubernetes + AWS
- **Machine Learning Engineer**: PyTorch + TensorFlow + MLflow

### **Real-World Projects**
- Build a SaaS application
- Create a data analytics platform
- Develop a recommendation system
- Build an IoT data processor

---

## 🎓 Resources

### **Documentation**
- [Python Official Docs](https://docs.python.org/3/)
- [Real Python](https://realpython.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/python/)

### **Communities**
- [Python Discord](https://discord.gg/python)
- [Reddit r/Python](https://reddit.com/r/Python)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/python)

### **Practice Platforms**
- [LeetCode](https://leetcode.com/)
- [HackerRank](https://www.hackerrank.com/domains/python)
- [Codewars](https://www.codewars.com/)

---

## 💡 Learning Tips

1. **Build Projects**: Apply concepts to real problems
2. **Read Code**: Study how experienced developers code
3. **Debug Actively**: Use debugger, not just print statements
4. **Test Everything**: Write tests as you code
5. **Optimize Gradually**: Don't premature optimize
6. **Document Well**: Future you will thank you
7. **Keep Learning**: Python evolves constantly

---

## 🎉 Congratulations!

You've completed Days 1-20 and are now an **Advanced Python Developer**! 🎊

You can now:
✅ Build production-ready applications
✅ Deploy to cloud services
✅ Analyze large datasets
✅ Create REST APIs
✅ Write tested, maintainable code
✅ Contribute to open source
✅ Mentor junior developers

---

<div align="center">

**Keep Coding. Keep Growing. Keep Shipping.** 🚀

**Your Python Journey Continues! 🐍✨**

[← Back to Days 1-10](./10_DAYS_PYTHON_LEARNING_SERIES.md)

</div>
