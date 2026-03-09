.PHONY: validate render all

all: render validate

render:
	python3 scripts/generate_register_views.py

validate:
	python3 scripts/validate_repo.py
