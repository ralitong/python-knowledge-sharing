run_tests: install_dependencies
	@echo "Running tests..."
	pytest

install_dependencies:
	@echo "Installing dependencies..."
	pip install -r requirements.txt
