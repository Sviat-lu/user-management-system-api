#!/usr/bin/env bash
# -*- coding: utf-8 -*-
template_env=../.env.template
main_env=../.env

if [[ ! -e ${main_env} ]]
then
    cp "${template_env}"  "${main_env}"
fi

docker compose -f docker/docker-compose.yml up --build
docker compose -f docker/docker-compose.yml down
