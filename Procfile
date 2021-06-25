web: python plpred/server.py --port $PORT --host 0.0.0.0 --model data/models/model.pickle
worker: celery -A plpred.worker.celery worker