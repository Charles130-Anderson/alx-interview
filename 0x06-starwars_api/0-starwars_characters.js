#!/usr/bin/node
/**
 * Prints all characters of a Star
 * Wars movie in proper order
 */

const request = require('request');
const movieId = process.argv[2];
const filmURL = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

/**
 * Fetch and print characters
 * of a given Star Wars film
 */
async function fetchAndPrintCharacters () {
  request(filmURL, async (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }
    const charURLList = JSON.parse(body).characters;
    for (const charURL of charURLList) {
      await new Promise((resolve, reject) => {
        request(charURL, (err, res, body) => {
          if (err) {
            console.error(err);
            return;
          }
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  });
}

fetchAndPrintCharacters();
