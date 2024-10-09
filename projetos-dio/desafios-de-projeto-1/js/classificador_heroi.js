const readline = require('readline');

// Configurando a interface para ler entradas do usuário
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function classificarHeroi() {
    rl.question("Quantos heróis deseja classificar? ", (numeroDeHerois) => {
        numeroDeHerois = parseInt(numeroDeHerois);

        let processarHeroi = (i) => {
            if (i < numeroDeHerois) {
                rl.question(`Digite o nome do herói ${i + 1}: `, (nome) => {
                    rl.question(`Digite a experiência (XP) do herói ${nome}: `, (xp) => {
                        xp = parseInt(xp);
                        let nivel;

                        if (xp < 1000) {
                            nivel = "Ferro";
                        } else if (xp <= 2000) {
                            nivel = "Bronze";
                        } else if (xp <= 5000) {
                            nivel = "Prata";
                        } else if (xp <= 7000) {
                            nivel = "Ouro";
                        } else if (xp <= 8000) {
                            nivel = "Platina";
                        } else if (xp <= 9000) {
                            nivel = "Ascendente";
                        } else if (xp <= 10000) {
                            nivel = "Imortal";
                        } else {
                            nivel = "Radiante";
                        }

                        console.log(`O Herói de nome ${nome} está no nível de ${nivel}`);
                        processarHeroi(i + 1);
                    });
                });
            } else {
                rl.close();  // Fecha o input do terminal
            }
        };

        processarHeroi(0);
    });
}

// Chama a função para classificar heróis
classificarHeroi();
