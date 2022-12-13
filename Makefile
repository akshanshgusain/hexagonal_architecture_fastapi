run:
	python -m uvicorn src.banking.adapters.entrypoints.application:app --host 0.0.0.0 --port 8001 --reload