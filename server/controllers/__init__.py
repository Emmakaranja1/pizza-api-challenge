def register_routes(app):
    @app.route('/')
    def index():
        return {'message': 'Pizza API is running!'}
