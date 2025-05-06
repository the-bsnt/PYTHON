# Writing a Docker Compose File

A Docker Compose file (typically named `docker-compose.yml`) allows you to define and run multi-container Docker applications. Here's a comprehensive guide to writing one:

## Basic Structure

```yaml
version: "3.8" # Compose file version
services: # Container definitions go here
  web:
    image: nginx:latest
    ports:
      - "80:80"
```

## Common Directives

### Service Definition

```yaml
services:
  app:
    image: myapp:1.0 # Use a pre-built image
    # build: ./dir         # Or build from Dockerfile in ./dir
    container_name: myapp # Custom container name
    restart: unless-stopped # Restart policy
```

### Networking

```yaml
ports:
  - "8080:80" # Host:Container port mapping
expose:
  - "3000" # Expose port to linked services
networks:
  - frontend
  - backend
```

### Volumes & Storage

```yaml
volumes:
  - ./data:/app/data # Bind mount
  - db_data:/var/lib/mysql # Named volume
environment:
  - DB_HOST=db
  - DB_PORT=5432
env_file:
  - .env # Load environment variables from file
```

### Dependencies & Links

```yaml
depends_on:
  - db
  - redis
links:
  - db:database # Legacy service linking
```

## Complete Example

```yaml
version: "3.8"

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - frontend
    depends_on:
      - app

  app:
    build: ./app
    environment:
      - NODE_ENV=production
    networks:
      - frontend
      - backend
    volumes:
      - ./app:/app
      - /app/node_modules

  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - backend

volumes:
  db_data:

networks:
  frontend:
  backend:
```

## Best Practices

1. Use specific version tags (not `latest`) for production
2. Define resource limits (cpu_shares, mem_limit)
3. Use named volumes for persistent data
4. Separate services into different networks for security
5. Use environment variables for configuration
6. Consider healthchecks for critical services

## Version Compatibility

- Version 3.x is recommended for current Docker Engine versions
- Version 2.x is legacy format
- Check Docker Engine compatibility with Compose file versions
