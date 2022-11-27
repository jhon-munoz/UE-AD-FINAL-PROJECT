FROM node:lts
WORKDIR /app
COPY . .
RUN npm install --omit=dev
RUN npm run build

CMD [ "node", "dist/index.js" ]
