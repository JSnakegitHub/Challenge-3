from api.main.home import app
from api.config import configurations


if __name__ == '__main__':
    config = configurations()
    config.create_tables
    app.run(debug=True, port=8080)
