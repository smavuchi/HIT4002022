# Passengers Prediction System
-The system consists of three major components which are web app, REST API and database.
-The following shows how to setup these components:

## Web Application:
-To run the App:
- Download and install Node 14.x
- Install Vue CLI using command 'npm install -g @vue/cli'
- Install required libraries in 'package.json' file using command 'npm install'
- Start the app using command 'npm run serve'

## API:
-Create '.env' file with credentials as follows:
- DATABASEUSER=""
- DATABASEPASSWORD=""
- DATABASE=""
- HOST="localhost:27017"
- JWT_SECRET_KEY=""

-Please fill blank "" with respective values

-To run the API:
- Install Python 3.x
- Create Python virtual environment in project's folder using command 'python -m venv myenv'
- Activate virtual environment using command 'ENV_NAME\scripts\activate'
- Install required libraries in 'requirements.txt' file using command 'pip install -r requirements.txt'
- Start the app using command 'flask run'

## Database:
-The system used MongoDB
-To configure the database:
- Download MongoDB server from their official site, link: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
- Create new database and use the credentials in the ".env" file mentioned earlier