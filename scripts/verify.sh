#!/bin/sh
set -eu
if [ -f go.mod ]; then go test ./...; elif [ -f requirements.txt ]; then pytest -q; elif [ -f pom.xml ]; then mvn test -q; else npm test -- --run; fi
