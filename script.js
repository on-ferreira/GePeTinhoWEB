// Aguarda o carregamento completo da página
window.onload = function() {

  // Obtém referências para os elementos da interface do usuário
  const chatList = document.querySelector('.chat-list');
  const chatHeader = document.querySelector('.chat-header h3');
  const chatMessages = document.querySelector('.chat-messages');
  const chatInput = document.querySelector('.chat-container .chat-input');
  const chatSendButton = document.querySelector('.chat-container .send-button');
  const settingsButton = document.querySelector('.settings .config');
  const clearButton = document.querySelector('.settings .clear');
  const configPopup = document.getElementById('settings-popup');

  // Adiciona uma mensagem de chat à seção de mensagens
  function addChatMessage(message, sender) {
    const chatMessages = document.querySelector('.chat-messages');
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message-container');
    if (sender === 'user') {
      messageContainer.classList.add('user-message');
      const p = document.createElement('p');
      p.textContent = message;
      messageContainer.appendChild(p);
    } else {
      messageContainer.classList.add('system-message');
      if (message instanceof Blob) {
        const img = document.createElement('img');
        img.src = URL.createObjectURL(message);
        messageContainer.appendChild(img);
      } else {
        const p = document.createElement('p');
        p.textContent = message;
        messageContainer.appendChild(p);
      }
    }
    chatMessages.appendChild(messageContainer);
  }

  // Adiciona um ouvinte de eventos de clique a cada item da lista de bate-papo
  chatList.querySelectorAll('li').forEach((chatItem, index) => {
    chatItem.addEventListener('click', function(event) {
      // Remove a classe "active" do item de bate-papo ativo atualmente
      chatList.querySelector('.active').classList.remove('active');
      // Adiciona a classe "active" ao item de bate-papo clicado
      chatItem.classList.add('active');
      // Define o cabeçalho do bate-papo para o nome do item de bate-papo clicado
      chatHeader.textContent = chatItem.querySelector('a').textContent;
      // Carrega as mensagens do bate-papo correspondente
      loadChatMessages(index);
    });
  });

  // Adiciona um ouvinte de eventos de clique ao botão Configurações
  settingsButton.addEventListener('click', function(event) {
    // Exibe o formulário de configurações
    document.getElementById('settings-popup').style.display = 'block';
  });

  // Adiciona um ouvinte de eventos de clique ao botão Limpar conversas
  clearButton.addEventListener('click', function(event) {
    // Limpa todas as mensagens do bate-papo atualmente exibido
    chatMessages.innerHTML = '';
  });

  
  document.querySelector("#settings-popup button[type='submit']").addEventListener("click", (event) => {
    event.preventDefault(); // Evita que o formulário seja enviado
    // Obtém a opção de tema selecionada pelo usuário
    const selectedTheme = document.querySelector("#settings-popup input[name='theme']:checked").value;
    // Define as cores primárias e secundárias com base na opção de tema selecionada
    let primaryColor, secondaryColor, borderColor, lightPrimaryColor, lightSecondaryColor,darkPrimaryColor;
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


  // Adiciona um ouvinte de eventos de clique ao botão Enviar
  chatSendButton.addEventListener('click', function(event) {
    // Adiciona a mensagem do usuário às mensagens do bate-papo
    addChatMessage('Usuário: '+chatInput.value, 'user');
    // Obtém uma imagem aleatória de gato usando a API Cataas
    fetch('https://cataas.com/cat/gif')
      .then(response => response.blob())
      .then(blob => {
        // Adiciona a imagem e as mensagens do sistema às mensagens do bate-papo
        addChatMessage(blob, 'system');
        addChatMessage('Gepetinho: Não sou capaz de entender o que você disse, que tal isso no lugar? '+'Meow '.repeat(15), 'system');
      });
      
    // Limpa o campo de entrada de texto
    chatInput.value = '';
  });
    
// Add event listener to input field to send message when Enter key is pressed
document.querySelector(".chat-input input").addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    event.preventDefault();
    document.querySelector(".chat-input button").click();
  }
});
}

