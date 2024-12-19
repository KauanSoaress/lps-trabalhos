async function callAPI(event) {
    event.preventDefault();

    const value = document.getElementById('values').value;

    // Chamar a API
    const response = await fetch('http://127.0.0.1:5000/value', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ value: value }) // Substitua pelo que deseja enviar
    });

    const result = await response.json();

    console.log(result);

    // Exibir a resposta na tag <p>
    const responseParagraph = document.getElementById('value-count');
    responseParagraph.textContent = 'This value was inputed ' + JSON.stringify(result['value_times']) + " time(s).";

    // Exibir a resposta
    const responseDiv = document.getElementById('result');
    responseDiv.style.display = 'block';
}