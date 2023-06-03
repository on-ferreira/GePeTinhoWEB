// Aguarda o carregamento completo da página
window.onload = function() {
  // Obtém referências para os elementos da interface do usuário
  const chatInput = document.querySelector('.chat-container .chat-input');
  const settingsButton = document.querySelector('.settings .config');
  const clearButton = document.querySelector('.settings .clear');
  const configPopup = document.getElementById('settings-popup');


  // Function to scroll down the chat container
  function scrollChatMessages() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Adiciona um ouvinte de eventos de clique ao botão Configurações
  settingsButton.addEventListener('click', function(event) {
    // Exibe o formulário de configurações
    document.getElementById('settings-popup').style.display = 'block';
  });


  document.querySelector("#settings-popup button[type='submit']").addEventListener("click", (event) => {
    event.preventDefault(); // Evita que o formulário seja enviado
    // Obtém a opção de tema selecionada pelo usuário
    const selectedTheme = document.querySelector("#settings-popup input[name='theme']:checked").value;
    // Define as cores primárias e secundárias com base na opção de tema selecionada
    let primaryColor, secondaryColor, borderColor, lightPrimaryColor, lightSecondaryColor, darkPrimaryColor;
    if (selectedTheme === "light") {
      primaryColor = "#282c34";
      secondaryColor = "#61dafb";
      borderColor = "#686969";
      lightPrimaryColor = "#575b64";
      lightSecondaryColor = "#92e5fc";
      darkPrimaryColor = "#5197d8";
    } else {
      primaryColor = "#61dafb";
      secondaryColor = "#282c34";
      borderColor = "#71bbff";
      lightPrimaryColor = "#92e5fc";
      lightSecondaryColor = "#575b64";
      darkPrimaryColor = "#000000";
    }
    // Atualiza as cores do tema
    document.documentElement.style.setProperty("--primary-color", primaryColor);
    document.documentElement.style.setProperty("--secondary-color", secondaryColor);
    document.documentElement.style.setProperty("--border-color", borderColor);
    document.documentElement.style.setProperty("--light-primary-color", lightPrimaryColor);
    document.documentElement.style.setProperty("--light-secondary-color", lightSecondaryColor);
    document.documentElement.style.setProperty("--darker-secondary-color", darkPrimaryColor);
    // Fecha a pop-up de configurações
    configPopup.style.display = 'none';
  });

}