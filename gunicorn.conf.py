import os

# Bind to the port that Render provides
bind = f"0.0.0.0:{os.environ.get('PORT', 8000)}"

# Number of worker processes
workers = 2

# Worker class for async support
worker_class = "uvicorn.workers.UvicornWorker"

# Timeout settings
timeout = 120
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"
