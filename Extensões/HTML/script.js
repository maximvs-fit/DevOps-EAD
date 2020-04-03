console.log("Olá Mundo")

var nome = "Ermirio Bonfim";
var idade = 30.5;
var cursos = ["ADS", "SI", "BD"];
var notas = [
    [7, 6, 5],
    [3.5, 4, 6],
    [8, 9, 10]
];




console.log("Olá " + nome)
console.log("idade " + idade + " anos")

for (var i = 0; i < cursos.length; i++) {
    console.log("Curso: " + cursos[i]);
    var media = 0;
    for (var j = 0; j < notas[i].length; j++) {
        media = media + notas[i][j];
    }

    media = media / 3;

    if (media >= 6) {
        console.log("Aprovado");
    } else {
        console.log("reprovado");
    }

}