from flask import Flask, render_template
from emailHandler import email_handler

def create_app():
  app = Flask(__name__,
    static_folder = "./dist/static",
    template_folder = "./dist"
  )
  app.register_blueprint(email_handler)
  return app

def add_vue_routes(app):
  @app.route('/')
  def serve_vue_app():
    """
    Serve our Vue app
    """
    return render_template('index.html')

  @app.after_request
  def add_header(req):
    """
    Clear cache for hot-reloading
    """
    req.headers["Cache-Control"] = "no-cache"
    return req

if __name__ == "__main__":
    app = create_app()
    add_vue_routes(app)
    app.run(debug=True)