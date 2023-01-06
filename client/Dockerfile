# pull official base image
FROM node:13.12.0-alpine

# set working directory
RUN mkdir -p /usr/client
WORKDIR /usr/client

# add app
COPY . ./

# add `/client/node_modules/.bin` to $PATH
ENV PATH /usr/client/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent



# start app
CMD ["npm", "start"]