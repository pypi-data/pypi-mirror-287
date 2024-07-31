import socketio
import joblib
import numpy as np

class VeoxServiceUnavailable(Exception):
    pass

class RemoteModel:
    def __init__(self, session_id, server_url):
        self.session_id = session_id
        self.server_url = server_url
        self.sio = socketio.Client()
        try:
            self.sio.connect(server_url)
        except socketio.exceptions.ConnectionError:
            raise VeoxServiceUnavailable("Veox service is unreachable at this moment. Please try again later.")
        self.status = 'initialized'

    def fit(self, X, y):
        self.sio.emit('fit', {
            'session_id': self.session_id,
            'X': joblib.dumps(X),
            'y': joblib.dumps(y)
        })

        @self.sio.on('progress')
        def on_progress(data):
            if data['session_id'] == self.session_id:
                print(f"Training progress: {data['progress']:.2f}%")

        @self.sio.on('fit_complete')
        def on_fit_complete(data):
            if data['session_id'] == self.session_id:
                self.status = 'trained'
                print("Training complete!")

        self.sio.wait()  # Wait for 'fit_complete' event
        return self

    def predict(self, X):
        if self.status != 'trained':
            raise ValueError("Model is not trained yet. Call fit() first.")

        self.sio.emit('predict', {
            'session_id': self.session_id,
            'X': joblib.dumps(X)
        })

        result = None

        @self.sio.on('predictions')
        def on_predictions(data):
            nonlocal result
            result = joblib.loads(data['predictions'])

        self.sio.wait()  # Wait for 'predictions' event
        return result

    def predict_proba(self, X):
        if self.status != 'trained':
            raise ValueError("Model is not trained yet. Call fit() first.")

        self.sio.emit('predict_proba', {
            'session_id': self.session_id,
            'X': joblib.dumps(X)
        })

        result = None

        @self.sio.on('probabilities')
        def on_probabilities(data):
            nonlocal result
            result = joblib.loads(data['probabilities'])

        self.sio.wait()  # Wait for 'probabilities' event
        return result

def init(key, server_url='http://x.veox.ai:5000'):
    try:
        response = requests.post(f'{server_url}/init', json={'key': key}, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise VeoxServiceUnavailable("Veox service is unreachable at this moment. Please try again later.")
    
    session_id = response.json()['session_id']
    return RemoteModel(session_id, server_url)
