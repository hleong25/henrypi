FROM node:16.10-alpine3.14

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@5.0.0 -g --silent

# add app
COPY . ./

RUN npm run build
RUN npm install -g serve

# start app
CMD ["serve", "-s", "build"]
