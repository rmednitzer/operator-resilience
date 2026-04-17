.PHONY: all render validate help

all:
	$(MAKE) render
	$(MAKE) validate

render:
	python3 scripts/generate_register_views.py

validate:
	python3 scripts/validate_repo.py

help:
	@echo "operator-resilience repository tools"
	@echo ""
	@echo "  make all      — render then validate (sequential)"
	@echo "  make render   — render Markdown register views from canonical YAML"
	@echo "  make validate — validate schemas, cross-references, and render drift"
