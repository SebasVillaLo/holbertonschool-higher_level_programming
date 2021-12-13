#!/usr/bin/node
function factorial (numero) {
  if (numero > 0) {
  numero = Math.abs(numero);
	return numero * factorial(numero - 1);
  }
  return 1;
}
const NUMBER = parseInt(process.argv[2]);
console.log(factorial(NUMBER));
