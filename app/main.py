from flask import Flask, jsonify

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/healthz")
    def health():
        return jsonify(status="ok", service="q005-herbal-alert")

    return app

app = create_app()
