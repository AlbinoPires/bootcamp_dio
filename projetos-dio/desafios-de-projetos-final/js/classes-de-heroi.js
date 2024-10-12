// Importa o pacote prompt-sync
const prompt = require('prompt-sync')();

// Classe generica de herói de aventura
class Heroi {
    constructor(nome, idade, tipo) {
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }

    // Método para realizar o ataque de acordo com o tipo do herói
    atacar() {
        let ataque;
        switch (this.tipo.toLowerCase()) {
            case 'mago':
                ataque = 'usou sua magia ensinada por Merlin';
                break;
            case 'guerreiro':
                ataque = 'usou espada sagrada Templária';
                break;
            case 'monge':
                ataque = 'usou suas artes marciais Kong-Fu';
                break;
            case 'ninja':
                ataque = 'usou suas técnicas Shuriken';
                break;
            default:
                ataque = 'realizou um ataque comum';
        }

        // Saída personalizada com o nome e detalhes do herói
        return `O ${this.tipo.charAt(0).toUpperCase() + this.tipo.slice(1)} ${this.nome} atacou usando ${ataque}\nClasse do Herói: ${this.tipo.charAt(0).toUpperCase() + this.tipo.slice(1)} - Nome: ${this.nome} - Idade: ${this.idade}`;
    }
}

// Função para interação com o usuário
function escolherHeroi() {
    const nome = prompt("Digite o nome do herói: ");
    const idade = prompt("Digite a idade do herói: ");
    const tipo = prompt("Escolha o tipo do herói (Mago, Guerreiro, Monge, Ninja): ");
    
    // Criando uma instância do herói com as entradas do usuário
    const heroiEscolhido = new Heroi(nome, idade, tipo);

    // Exibindo o resultado do ataque
    console.log(heroiEscolhido.atacar());
}

// Inicia a interação com o usuário
escolherHeroi();
