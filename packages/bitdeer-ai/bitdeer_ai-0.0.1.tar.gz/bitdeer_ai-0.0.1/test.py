from bitdeer_ai.training.client import TrainingClient

client = TrainingClient(host='test-api.bitdeer.ai:443', token="f81480c533608028a9fb1c8635661ea18065b8c0651786d8")

jobs = client.list_training_jobs()

print(jobs)