#!/usr/bin/env bash

# Script to generate Python classes from GraphQL schema

SCHEMA='https://github.com/ajberdy/ai-city-server/raw/master/src/schema.graphql'
TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjanpxMmwxbDhjdjN3MDc5NGFpZ2JqbjZnIiwiaWF0IjoxNTY2OTMxNzIzfQ.7XXG35OBDqGvs9cGKspLwAi4D02_UT5NCB1Ccn4D2pQ'

python3 -m sgqlc.introspection \
  --exclude-deprecated \
  -H "Authorization: ${TOKEN}" \
  https://ai-city-server.herokuapp.com \
  graphql-schema.json

sgqlc-codegen graphql-schema.json graphql_schema.py
