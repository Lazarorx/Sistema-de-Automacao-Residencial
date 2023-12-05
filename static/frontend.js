// Função para enviar comandos ao backend
async function sendCommand(device, action) {
    try {
        const response = await fetch(`/api/${device}/command`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action }),
        });

        const result = await response.json();
        console.log(`${device}: ${result.status}`);
    } catch (error) {
        console.error(`Erro ao enviar comando para ${device}: ${error.message}`);
    }
}

// Funções de clique para os botões
document.getElementById('lightOn').addEventListener('click', () => sendCommand('light', 'on'));
document.getElementById('lightOff').addEventListener('click', () => sendCommand('light', 'off'));

document.getElementById('setTemperature').addEventListener('click', () => {
    const temperature = document.getElementById('temperature').value;
    sendCommand('thermostat', `set_temperature(${temperature})`);
});

document.getElementById('toggleSecurity').addEventListener('click', () => sendCommand('security', 'toggle'));
document.getElementById('toggleBlinds').addEventListener('click', () => sendCommand('blinds', 'toggle'));
