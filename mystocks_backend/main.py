from app import create_app 

app = create_app()

if __name__ == '__main__':
	app.run(port=5000,host='0.0.0.0')
# from app import create_app as application

# if __name__ == '__main__':
# 	application.run()

@app.route("/")
def index():
  return app.send_static_file('index.html')