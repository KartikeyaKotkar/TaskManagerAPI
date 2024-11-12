from app import create_app

app = create_app(config_name="development")
app.run(debug=True)
