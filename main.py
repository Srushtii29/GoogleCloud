import webapp2
import jinja2

# Set up Jinja2 template environment
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'))

class CalculatorHandler(webapp2.RequestHandler):
    def get(self):
        # Render the calculator form using Jinja2 template
        template = jinja_env.get_template('calculator.html')
        self.response.write(template.render())

    def post(self):
        # Get user input from calculator form
        num1 = float(self.request.get('num1'))
        num2 = float(self.request.get('num2'))
        operator = self.request.get('operator')

        # Perform calculation based on selected operator
        if operator == 'add':
            result = num1 + num2
        elif operator == 'subtract':
            result = num1 - num2
        elif operator == 'multiply':
            result = num1 * num2
        elif operator == 'divide':
            result = num1 / num2

        # Render the result using Jinja2 template
        template = jinja_env.get_template('result.html')
        self.response.write(template.render({'result': result}))

app = webapp2.WSGIApplication([
    ('/', CalculatorHandler),
], debug=True)
