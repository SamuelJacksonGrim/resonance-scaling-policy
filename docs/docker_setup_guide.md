> **Copyright 2026 Samuel Jackson Grim** > **Architect of Resonance** > Licensed under the Apache License, Version 2.0. See [LICENSE](https://github.com/SamuelJacksonGrim/resonance-scaling-policy/blob/main/LICENSE) for details.

---

# Docker Setup Guide for Resonance Scaling Policy

## Prerequisites
- Docker installed
- Docker Compose installed

## Build and Run
1. Build the image: `docker build -t rsp-v1 .`
2. Run the container: `docker run -p 8000:8000 rsp-v1`
   - Or with Docker Compose: `docker-compose up`

## Development Mode
Use Docker Compose with --reload for hot-reloading during dev.

## Database Integration (Optional)
If using PostgreSQL for Nexus:
- Update prometheus/nexus_stub.py to connect to db.
- Environment vars in docker-compose for DB creds.

This setup containerizes the full orchestrator, making RSP deployable on any cloud/host.
