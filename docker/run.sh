#!/bin/bash
echo "Starting AINEXUS ecosystem..."
docker-compose up -d

echo "Waiting for services to start..."
sleep 10

echo "✅ Services started:"
echo "   - AINEXUS API: http://localhost:8000"
echo "   - Prometheus:  http://localhost:9090"
echo "   - Grafana:     http://localhost:3000 (admin/admin)"
echo "   - Redis:       localhost:6379"

echo "Check logs with: docker-compose logs -f ainexus"
