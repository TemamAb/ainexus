#!/bin/bash
echo "Building AINEXUS Docker image..."
docker build -t ainexus:latest .

if [ $? -eq 0 ]; then
    echo "✅ AINEXUS image built successfully"
    echo "Run with: docker-compose up -d"
else
    echo "❌ Build failed"
    exit 1
fi
