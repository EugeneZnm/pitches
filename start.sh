#!/usr/bin/env bash
export SECRET_KEY='1234'
export SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://eugene:necromancer@localhost/final'
export MAIL_USERNAME=testsznm@gmail.com
export MAIL_PASSWORD=t3stsznm1.
python3.6 manage.py server