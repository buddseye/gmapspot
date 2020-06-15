FROM electronuserland/builder:wine

COPY ./package.json ./index.html ./check-spots.json ./main.js ./
RUN yarn install
VOLUME ~/dist
CMD yarn build
