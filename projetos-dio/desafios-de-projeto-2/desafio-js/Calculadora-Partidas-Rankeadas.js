// Import readline module to read user input
// Importa o módulo readline para ler a entrada do usuário
const readline = require('readline');

// Configure readline to use input and output from the terminal
// Configura o readline para usar entrada e saída do terminal
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to calculate the rank based on the number of victories
// Função para calcular a classificação com base no número de vitórias
function calcularClassificacao(vitorias) {
    let classificacao;

    // Determine the rank based on the number of victories
    // Determina a classificação com base no número de vitórias
    if (vitorias < 10) {
        classificacao = "Ferro";
    } else if (vitorias >= 11 && vitorias <= 20) {
        classificacao = "Bronze";
    } else if (vitorias >= 21 && vitorias <= 50) {
        classificacao = "Prata";
    } else if (vitorias >= 51 && vitorias <= 80) {
        classificacao = "Ouro";
    } else if (vitorias >= 81 && vitorias <= 90) {
        classificacao = "Diamante";
    } else if (vitorias >= 91 && vitorias <= 100) {
        classificacao = "Lendário";
    } else {
        classificacao = "Imortal";
    }

    return classificacao; // Return the calculated rank / Retorna a classificação calculada
}

// Function to calculate the balance of victories and losses
// Função para calcular o saldo de vitórias e derrotas
function calcularSaldoPartidas(vitorias, derrotas) {
    return vitorias - derrotas; // Calculate the balance as victories minus losses / Calcula o saldo como vitórias menos derrotas
}

// Main function to execute the program logic
// Função principal para executar a lógica do programa
function main() {
    // Input: Number of victories and losses
    // Entrada: Número de vitórias e derrotas
    rl.question("Digite o número de vitórias: ", (vitorias) => {
        rl.question("Digite o número de derrotas: ", (derrotas) => {
            // Convert the input values to integers
            // Converte os valores de entrada para inteiros
            vitorias = parseInt(vitorias);
            derrotas = parseInt(derrotas);

            // Calculate the balance and the rank
            // Calcula o saldo e a classificação
            const saldo = calcularSaldoPartidas(vitorias, derrotas);
            const classificacao = calcularClassificacao(vitorias);

            // Output the result
            // Saída: Exibe o resultado
            console.log(`O Herói tem um saldo de partidas de ${saldo} e está classificado como ${classificacao}.`);

            // Close the readline interface
            // Fecha a interface readline
            rl.close();
        });
    });
}

// Call the main function to execute the program
// Chama a função principal para executar o programa
main();
