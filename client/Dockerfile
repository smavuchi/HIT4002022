FROM node:14.0.0

#create working directory
WORKDIR /decentralizedvoting/src/client

#copy package.json & package lock into our working directory...* helps copying both
COPY package*.json ./

#install node dependencies
RUN npm install

#copy everything on line 10 into our container
COPY . .

#expose the port we're using
EXPOSE 3000

#our command for runnning the app
CMD ["npm", "start"]