from app.application import create_app

app = create_app(debug=True)

if __name__ == "__main__":
  app.run("0.0.0.0")