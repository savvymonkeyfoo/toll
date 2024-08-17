import streamlit as st

# Define the HTML code for the full-page Flowise chatbot with custom styles
flowise_html = """
<flowise-fullchatbot></flowise-fullchatbot>
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js";
    Chatbot.initFull({
        chatflowid: "0b815c16-cfc0-41d9-91ce-d5bd9cb76d89",
        apiHost: "https://flowise-yvjw.onrender.com",
        theme: {
            chatWindow: {
                showTitle: true,
                title: 'Toll Solutions and Case Study Email Writer',
                titleAvatarSrc: 'https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/google-messages.svg',
                showAgentMessages: true,
                welcomeMessage: 'Hello! Who are we writing an email to today?',
                errorMessage: 'This is a custom error message',
                backgroundColor: "#f4f4f4",
                height: 700,
                width: '100%',
                fontSize: 16,
                poweredByTextColor: "#ffffff",
                botMessage: {
                    backgroundColor: "#e0e7ff",
                    textColor: "#303235",
                    showAvatar: true,
                    avatarSrc: "https://cdn-icons-png.flaticon.com/512/2021/2021646.png",
                },
                userMessage: {
                    backgroundColor: "#007a68",
                    textColor: "#ffffff",
                    showAvatar: true,
                    avatarSrc: "https://raw.githubusercontent.com/zahidkhawaja/langchain-chat-nextjs/main/public/usericon.png",
                },
                textInput: {
                    placeholder: 'Type your question here...',
                    backgroundColor: '#ffffff',
                    textColor: '#303235',
                    sendButtonColor: '#007a68',
                    maxChars: 50,
                    maxCharsWarningMessage: 'You have exceeded the character limit.',
                    autoFocus: true,
                    sendMessageSound: true,
                    receiveMessageSound: true,
                },
                feedback: {
                    color: '#303235',
                },
                footer: {
                    textColor: '#303235',
                    text: 'Made by',
                    company: 'Capgemini',
                    companyLink: 'https://capgemini.com',
                }
            },
            button: {
                backgroundColor: "#007a68",
                right: 20,
                bottom: 20,
                size: 48, // small | medium | large | number
                dragAndDrop: true,
                iconColor: "white",
                customIconSrc: "https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/google-messages.svg",
            },
            tooltip: {
                showTooltip: true,
                tooltipMessage: 'Hi There 👋!',
                tooltipBackgroundColor: 'black',
                tooltipTextColor: 'white',
                tooltipFontSize: 16,
            }
        }
    });
</script>
"""
# Optionally, add a title or description
st.title("Toll Email Writer")
st.write("Helps write emails for Account Managers with solutions and case studies.")

# Embed the full-page Flowise chatbot in Streamlit
st.components.v1.html(flowise_html, height=800)

